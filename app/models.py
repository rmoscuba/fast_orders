from pydantic import BaseModel, validator
from decimal import Decimal
from typing import List

class Item(BaseModel):
    id: int
    item: str | None = None
    quantity: int
    price: Decimal | None = None
    status: str | None = None

    @validator("price")
    def validate_price(cls, v):
        if v < 0:
            raise ValueError("Price must be anpositive Decimal value")
        return v
    
    @validator("status")
    def validate_status(cls, v):
        if v not in ['completed','pending','canceled']:
            raise ValueError("Status must be 'completed','pending' or 'canceled'")
        return v

class OrderList(BaseModel):
    orders: List[Item]
    criterion: str | None = None

    @validator("criterion")
    def validate_status(cls, v):
        if v not in ['completed','pending','canceled','all']:
            raise ValueError("Status must be 'completed','pending', 'canceled' or 'all'")
        return v
