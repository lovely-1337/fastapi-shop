from typing import Optional

from pydantic import BaseModel, Field


class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(default=1, ge=1)


class CartItemUpdate(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)


class CartItem(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int
    subtotal: float
    image_url: Optional[str] = None


class CartResponse(BaseModel):
    items: list[CartItem]
    total_price: float
    item_count: int