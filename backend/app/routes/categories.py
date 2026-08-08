from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from ..services.category_services import CategoryService
from ..schemas.category import CategoryCreate

router= APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("", response_model=List[CategoryCreate], status_code=status.HTTP_200_OK)
def get_categories(db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    return category_service.get_all_categories() 

@router.get("/{category_id}", response_model=CategoryCreate, status_code=status.HTTP_200_OK)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    return category_service.get_category_by_id(category_id)