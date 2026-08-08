from typing import Dict

from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.cart import CartItemCreate, CartItemUpdate, CartResponse
from ..services.cart_services import CartService


router = APIRouter(
    prefix="/cart",
    tags=["cart"],
)


class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart_data: Dict[int, int]


class UpdateCartItemRequest(BaseModel):
    product_id: int
    quantity: int
    cart_data: Dict[int, int]


@router.post("/add", response_model=Dict[int, int])
def add_to_cart(
    request: AddToCartRequest,
    db: Session = Depends(get_db),
):
    service = CartService(db)

    cart_item = CartItemCreate(
        product_id=request.product_id,
        quantity=request.quantity,
    )

    return service.add_to_cart(request.cart_data, cart_item)


@router.post("", response_model=CartResponse)
def get_cart(
    cart_data: Dict[int, int],
    db: Session = Depends(get_db),
):
    service = CartService(db)
    return service.get_cart_details(cart_data)


@router.put("/update", response_model=Dict[int, int])
def update_cart_item(
    request: UpdateCartItemRequest,
    db: Session = Depends(get_db),
):
    service = CartService(db)

    cart_item = CartItemUpdate(
        product_id=request.product_id,
        quantity=request.quantity,
    )

    return service.update_cart_item(request.cart_data, cart_item)