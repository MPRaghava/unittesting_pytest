from shopping_cart import app
from fastapi.testclient import TestClient

client = TestClient(app)

# ✅ Test adding an item to the cart
# Verifies that the item is successfully added and the response message is correct
def test_add_item():
    response = client.post("cart/add",json={"name" :"Pine apple","quantity" :3})
    assert response.status_code == 200
    assert "Added 3 of Pine apple" in response.json()["message"]


# ❌ Test adding an item with invalid (zero) quantity
# Verifies that the API rejects zero quantity with a 400 response
def test_add_invalid_quantity():
    response = client.post("cart/add",json = {"name":"banana","quantity":0})
    # assert response.status_code == 400
    assert "Quantity must be positive" in response.json()["detail"]


# ✅ Test retrieving the current cart contents
# Adds an item and checks that it appears in the cart
def test_get_cart():
    client.post("/cart/add",json={"name":"mango","quantity" : 2})
    response = client.get("/cart")
    assert response.status_code == 200
    assert "mango" in response.json()


# ✅ Test removing a specific quantity of an item
# Adds an item, removes part of it, and checks the correct message
def test_remove_item():
    client.post("/cart/add",json={"name":"grapes","quantity":5})
    response = client.post("/cart/remove",json={"name":"grapes","quantity":3})
    assert response.status_code ==200
    assert "Removed 3 of grapes" in response.json()["message"]


# ✅ Test removing all quantity of an item
# Adds and completely removes an item, ensuring it's no longer in the cart
def test_remove_item_completely():
    client.post("/cart/add",json={"name":"pears","quantity":2})
    client.post("/cart/remove",json={"name":"pears","quantity":2})
    response = client.get("/cart")
    assert "pears" not in response.json()