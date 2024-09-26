### 1 Go to https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html
### 2 You need to collect all of the items on the menu
### 3 Fields to collect:
    -name
    -description
    -calories
    -fats
    -carbs
    -proteins
    -unsaturated fats
    -sugar
    -salt
    -portion

### 4 The data should be saved locally in a json file
### 5 Write few endpoints on one of the following libs ( Flask, FastAPI )
    -get: /all_products/  - return all information about all products
    -get: /products/{product_name}  - return information about exact product
    -get: //products/{product_name}/{product_field}  - return information about exact field  exact product



Here’s a well-structured section for your GitHub README that explains how the project works:

---

## How It Works

### Running the Scraper

To gather data from the website and save it to a JSON file, run the `mc_donalds.py` script. Use the following command:

```bash
python mc_donalds.py
```

After executing this command, the collected data will be stored in a file named `products.json`.

### Running the FastAPI Server

The FastAPI server utilizes the data from `products.json` to provide access through a RESTful API. To start the server, run the following command:

```bash
uvicorn main:app --reload
```

### API Endpoints

Once the FastAPI server is running, you can use the following API endpoints:

- **Get All Products**  
  `GET /all_products/`  
  Returns all information about all products.

- **Get Specific Product**  
  `GET /products/{product_name}`  
  Returns detailed information about a specific product.

- **Get Specific Field of a Product**  
  `GET /products/{product_name}/{product_field}`  
  Returns the specified field of a specific product.

---

