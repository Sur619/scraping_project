import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException


# Function to get menu items
def get_menu_items(driver):
    return driver.find_elements(By.CSS_SELECTOR, "ul.cmp-category__row li.cmp-category__item")


# Function to extract element
def extract_element(driver, selector, default_value="Description not available", use_text=False):
    try:
        element = driver.find_element(By.XPATH, selector)
        if use_text:
            value = element.text.strip()
        else:
            value = element.get_attribute('innerText').strip()

        value = value.replace("\n", " ").replace("\xa0", " ")
        value = ' '.join(value.split())
        return value
    except NoSuchElementException:
        return default_value


# Function to collect product details
def collect_product_details(driver, item):
    item.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.cmp-product-details-main__mobile-head"))
    )
    time.sleep(0.5)

    name = extract_element(driver, "//span[@class='cmp-product-details-main__heading-title']", "Name not available")
    description = extract_element(driver, "//div[@class='cmp-text']", "Description not available", use_text=True)
    fats = extract_element(driver, "//span[@class='sr-only sr-only-pd' and contains(text(), 'Жири')]", "Fats")
    calories = extract_element(driver, "//span[@class='sr-only sr-only-pd' and contains(text(), 'ккал Калорійність')]",
                               "Calories")
    carbs = extract_element(driver, "//span[@class='sr-only sr-only-pd' and contains(text(), 'г Вуглеводи')]", "Carbs")
    proteins = extract_element(driver, "//span[@class='sr-only sr-only-pd' and contains(text(), 'г Білки')]",
                               "Proteins")
    unsaturated_fats = extract_element(
        driver,
        "//span[contains(text(), 'НЖК:')]/../span[@class='value']/span[@aria-hidden='true']", "Unsaturated Fats")
    sugar = extract_element(
        driver,
        "//li[@class='label-item' and .//span[@class='metric' and text()='Цукор:']]/span[@class='value']/span[@aria-hidden='true' and contains(text(), 'г/g') and contains(text(), '% DV')]",
        "Sugar")
    salt = extract_element(driver,
                           "//span[contains(text(), 'Сіль:')]/../span[@class='value']/span[@aria-hidden='true']",
                           "Salt")
    portion = extract_element(driver,
                              "//span[contains(text(), 'Порція:')]/../span[@class='value']/span[@aria-hidden='true']",
                              "Portion")

    driver.back()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.cmp-category__row")))

    return {
        'name': name,
        'description': description,
        'fats': fats,
        'calories': calories,
        'carbs': carbs,
        'proteins': proteins,
        'unsaturated_fats': unsaturated_fats,
        'sugar': sugar,
        'salt': salt,
        'portion': portion
    }


def main():
    # Initialize the webdriver
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get('https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html')

    # Collect product details
    product_details = []
    menu_items = get_menu_items(driver)

    for index in range(len(menu_items)):
        try:
            print(f"Collecting information about product {index + 1}/{len(menu_items)}")
            menu_items = get_menu_items(driver)
            if index >= len(menu_items):
                break
            item = menu_items[index]
            details = collect_product_details(driver, item)
            product_details.append(details)
            print(details)
        except (StaleElementReferenceException, TimeoutException) as e:
            print(f"Error processing product: {e}")

    # Save the product details to a JSON file
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(product_details, f, ensure_ascii=False, indent=4)

    driver.quit()
    print("Data saved to products.json")


if __name__ == "__main__":
    main()
