from pydantic import BaseModel
from decimal import Decimal
from typing import List

class Item(BaseModel):
    id: int
    item: str | None = None
    quantity: int
    price: Decimal | None = None
    status: str | None = None

class OrderList(BaseModel):
    orders: List[Item]
    criterion: str | None = None
