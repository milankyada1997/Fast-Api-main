from fastapi import APIRouter, Request
from controllers.OrderControllers import store_order_controller

router = APIRouter()

@router.post("/orders/")
async def create_order(request: Request):
    body = await request.json()
    return store_order_controller(body)
