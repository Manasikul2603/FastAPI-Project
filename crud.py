from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

class Product(BaseModel):
    product_id:int
    product_name:str
    price:float
    Quantity:int


products=[{"product_id": 1, "product_name": "Laptop", "price": 50000, "Quantity": 10},
    {"product_id": 2, "product_name": "Mobile", "price": 30000, "Quantity": 20}
    ]
@app.get("/products/{product_id}")
def get_product(product_id:int):
    for product in products:
        if product['product_id']==product_id:
            return {"product":product}
    raise HTTPException(status_code=404,detail="Product not found")


@app.delete("/products/{product_id}")
def delete_product(product_id:int):
    for product in products:
        if product['product_id']==product_id:
            products.remove(product)
        return {'message':'Product deleted successfully'}
    raise HTTPException(status_code=404,detail="Product not found")