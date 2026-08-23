from fastapi import FastAPI
from sqlalchemy import text
from app.routes.orders import route as orders_router

from app.settings.database.database import engine

app = FastAPI()
app.include_router(orders_router, prefix="/orders")

@app.get("/health")
def health():
    with engine.connect() as connection:
        db_status = connection.execute(text("SELECT 1"))
        return {
                "status": "ok",
                "database status": db_status.scalar()
            }