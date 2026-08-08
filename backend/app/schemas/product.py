from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=200, description="Product name")
    description: Optional[str] = Field(None, max_length=500, description="Product description")
    price: int = Field(..., gt=0, description="Product price in cents")
    image_url: Optional[str] = Field(None, description="URL of the product image")
    category_id: int = Field(..., description="ID of the category this product belongs to")

class ProductCreate(ProductBase):  
    pass
class ProductResponse(ProductBase):
    id: int = Field(..., description="Unique Product ID")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse = Field(..., description="Category details for the product")

    class Config:
        from_attributes = True

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(..., description="Total number of products")