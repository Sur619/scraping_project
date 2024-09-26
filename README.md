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
