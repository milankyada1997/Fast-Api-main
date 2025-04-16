from fastapi import HTTPException
from datetime import datetime
from  config.database import order_collection

def store_order_controller(order_data: dict):
    try:
        order_data["created_at"] = datetime.now().isoformat()
        order_collection.insert_one(order_data)
        return {"message": "Order stored successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
