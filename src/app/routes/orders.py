from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.order import OrderCreate, OrderResponse, OrderUpdate
from app.service.orders import (
    create_order,
    delete_order,
    get_all_orders,
    get_order,
    update_order,
)
from app.settings.database.database import SessionLocal


def get_db():
    """Dependency for database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


route = APIRouter()


@route.get("", response_model=list[OrderResponse])
def list_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all orders with pagination"""
    return get_all_orders(db, skip=skip, limit=limit)


@route.get("/{order_id}", response_model=OrderResponse)
def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    """Get a single order by ID"""
    db_order = get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@route.post("", response_model=OrderResponse, status_code=201)
def create_new_order(order: OrderCreate, db: Session = Depends(get_db)):
    """Create a new order"""
    return create_order(db, order)


@route.put("/{order_id}", response_model=OrderResponse)
def update_existing_order(
    order_id: int, order: OrderUpdate, db: Session = Depends(get_db)
):
    """Update an existing order"""
    db_order = update_order(db, order_id, order)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@route.delete("/{order_id}", status_code=204)
def delete_existing_order(order_id: int, db: Session = Depends(get_db)):
    """Delete an order"""
    success = delete_order(db, order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
