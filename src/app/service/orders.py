
from sqlalchemy.orm import Session
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate


def create_order(db: Session, order_data: OrderCreate) -> Order:
    """Create a new order in the database"""
    db_order = Order(
        product_name=order_data.product_name,
        quantity=order_data.quantity,
        unit_price=order_data.unit_price,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order(db: Session, order_id: int) -> Order | None:
    """Get a single order by ID"""
    return db.query(Order).filter(Order.id == order_id).first()


def get_all_orders(db: Session, skip: int = 0, limit: int = 100) -> list[Order]:
    """Get all orders with pagination"""
    return db.query(Order).offset(skip).limit(limit).all()


def update_order(db: Session, order_id: int, order_data: OrderUpdate) -> Order | None:
    """Update an order by ID"""
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        return None
    
    update_data = order_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_order, key, value)
    
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int) -> bool:
    """Delete an order by ID"""
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        return False
    
    db.delete(db_order)
    db.commit()
    return True