# shopping_cart.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory cart (simulate DB)
cart: Dict[str, int] = {}

class Item(BaseModel):
    name: str
    quantity: int

@app.post("/cart/add")
def add_item(item: Item):
    if item.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be positive")
    cart[item.name] = cart.get(item.name, 0) + item.quantity
    return {"message": f"Added {item.quantity} of {item.name}"}

@app.post("/cart/remove")
def remove_item(item: Item):
    if item.name not in cart:
        raise HTTPException(status_code=404, detail="Item not found in cart")
    if item.quantity <= 0 or item.quantity > cart[item.name]:
        raise HTTPException(status_code=400, detail="Invalid quantity")
    cart[item.name] -= item.quantity
    if cart[item.name] == 0:
        del cart[item.name]
    return {"message": f"Removed {item.quantity} of {item.name}"}

@app.get("/cart")
def get_cart():
    return cart
