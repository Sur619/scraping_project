from fastapi import FastAPI, HTTPException
import json

app = FastAPI()


def load_product_data():
    with open('products.json', 'r', encoding='utf-8') as f:
        return json.load(f)

products_data = load_product_data()

# return all information about all products
@app.get("/all_products/")
def get_all_products():
    return products_data

# return information about exact product
@app.get("/products/{product_name}")
def get_product(product_name: str):
    for product in products_data:
        if product['name'] == product_name:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# return information about exact field  exact product
@app.get("/products/{product_name}/{product_field}")
def get_product_field(product_name: str, product_field: str):
    for product in products_data:
        if product['name'] == product_name:
            if product_field in product:
                return {product_field: product[product_field]}
            else:
                raise HTTPException(status_code=404, detail="Field not found")
    raise HTTPException(status_code=404, detail="Product not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
