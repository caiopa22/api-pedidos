from fastapi import APIRouter

route = APIRouter()

@route.get("/orders")
def get_orders():
    return {"message": "List of orders"}
