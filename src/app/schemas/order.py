from datetime import datetime

from pydantic import BaseModel


class Order(BaseModel):
    id: int
    product_name: str
    quantity: int
    price: float
    created_at: datetime