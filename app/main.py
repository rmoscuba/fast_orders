from fastapi import FastAPI

from app.models import OrderList
from app.orders import process_orders

app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.post("/solution")
async def post_solution(data: OrderList):
    total_revenue = process_orders(data.orders, data.criterion)
    return f'{total_revenue:.2f}'