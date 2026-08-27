from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    """Schema for creating a new order"""
    product_name: str = Field(..., min_length=1, max_length=255)
    quantity: int = Field(..., gt=0)
    unit_price: float = Field(..., gt=0)


class OrderUpdate(BaseModel):
    """Schema for updating an order"""
    product_name: Optional[str] = Field(None, min_length=1, max_length=255)
    quantity: Optional[int] = Field(None, gt=0)
    unit_price: Optional[float] = Field(None, gt=0)


class OrderResponse(BaseModel):
    """Schema for order responses"""
    id: int
    product_name: str
    quantity: int
    unit_price: float
    created_at: datetime

    model_config = {"from_attributes": True}