from fastapi import FastAPI

from app.models import OrderList

app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.post("/solution")
async def post_solution(orders: OrderList):
    raise NotImplementedError