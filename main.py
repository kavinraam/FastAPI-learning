from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session, engine
from sqlalchemy.orm import Session
import db_models

db_models.Base.metadata.create_all(bind= engine)

app = FastAPI()

app.add_middleware( CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"])

products = [ Product(id = 1, name = "Phone", description = "Budget phone", price = 99, quantity = 10),
            Product(id = 2, name = "Laptop", description = "Budget laptop", price = 999, quantity = 7),
            Product(id = 3, name = "Iphone", description = "Premium phone", price = 199, quantity = 5)
            ]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(db_models.Product).count
    if count == 0:
        for product in products:
            db.add(db_models.Product(**product.model_dump()))

        db.commit()

init_db()

@app.get("/")
def greet():
    return "Hi Buddy, Welcome to the Arena!"

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(db_models.Product).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
            return db_product
    return "Product not found!"

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(db_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
            db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
            if db_product:
                db_product.name = product.name
                db_product.description = product.description
                db_product.price = product.price
                db_product.quantity = product.quantity
                db.commit()
                return "Product updated successfully!"
            else:
                return "Product not found!"

@app.delete("/products")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
         db.delete(db_product)
         db.commit()
         return "Deletion successful!"
    else:
        return "Product not found!"


