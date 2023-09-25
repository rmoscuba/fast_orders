import json
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

json_orders_data_str_2399_55 = """{
   "orders": [
       {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
       {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
       {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
       {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
   ],
   "criterion": "all"
}
"""

json_orders_data_str_1299_69 = """{
   "orders": [
       {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
       {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
       {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
       {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
   ],
   "criterion": "completed"
}
"""

json_orders_data_str_999_90= """{
   "orders": [
       {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
       {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
       {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
       {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
   ],
   "criterion": "pending"
}
"""

json_orders_data_str_1024_89= """{
   "orders": [
       {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
       {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
       {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
       {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"},
       {"id": 5, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "pending"}
   ],
   "criterion": "pending"
}
"""

json_orders_data_str_negative_price = """{
   "orders": [
       {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
       {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
       {"id": 3, "item": "Headphones", "quantity": 3, "price": -99.90, "status": "completed"},
       {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
   ],
   "criterion": "completed"
}
"""

json_orders_data_str_bad_criterion = """{
   "orders": [
       {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
       {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
       {"id": 3, "item": "Headphones", "quantity": 3, "price": -99.90, "status": "completed"},
       {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
   ],
   "criterion": "bad_criterion"
}
"""

json_orders_data_str_bad_status = """{
   "orders": [
       {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
       {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
       {"id": 3, "item": "Headphones", "quantity": 3, "price": -99.90, "status": "completed"},
       {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "bad_status"}
   ],
   "criterion": "completed"
}
"""

def test_orders_all():
    json_orders_data = json.loads(json_orders_data_str_2399_55)
    response = client.post("/solution", json=json_orders_data)
    assert response.status_code == 200
    assert response.text =='"2399.55"'

def test_orders_completed():
    json_orders_data = json.loads(json_orders_data_str_1299_69)
    response = client.post("/solution", json=json_orders_data)
    assert response.status_code == 200
    assert response.text =='"1299.69"'

def test_orders_pending():
    json_orders_data = json.loads(json_orders_data_str_999_90)
    response = client.post("/solution", json=json_orders_data)
    assert response.status_code == 200
    assert response.text =='"999.90"'

def test_orders_validate_negative_price():
    json_orders_data = json.loads(json_orders_data_str_negative_price)
    response = client.post("/solution", json=json_orders_data)
    assert response.status_code == 422

def test_orders_validate_bad_criterion():
    json_orders_data = json.loads(json_orders_data_str_bad_criterion)
    response = client.post("/solution", json=json_orders_data)
    assert response.status_code == 422

def test_orders_validate_bad_status():
    json_orders_data = json.loads(json_orders_data_str_bad_status)
    response = client.post("/solution", json=json_orders_data)
    assert response.status_code == 422
