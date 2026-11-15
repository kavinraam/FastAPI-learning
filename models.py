from pydantic import BaseModel #Pydantic is a Python library used for data validation, parsing, and serialization

class Product(BaseModel): #Inheriting the BaseModel class
    id : int
    name : str
    description : str
    price : float
    quantity : int
