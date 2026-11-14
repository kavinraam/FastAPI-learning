from fastapi import FastAPI
from models import Product

app = FastAPI()

products = [ Product(id = 1, name = "Phone", description = "Budget phone", price = 99, quantity = 10),
            Product(id = 2, name = "Laptop", description = "Budget laptop", price = 999, quantity = 7),
            Product(id = 3, name = "Iphone", description = "Premium phone", price = 199, quantity = 5)
            ]

@app.get("/")
def greet():
    return "Hi Buddy, Welcome to the Arena!"

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product

    return "Product not found!"

@app.post("/product")
def add_product(product: Product):
    products.append(product)

    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product added successfully!"

    return "Product not found!"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted successfully!"

    return "Product not found!"
