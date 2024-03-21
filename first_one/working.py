from typing import Annotated, Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


inventory = {}

@app.get("/get-item/{item_id}")
async def get_item(item_id: int):
    return inventory[item_id]




@app.get("/get-by-name")
async def get_item(name: str = Query(None, title="Name", description="Name of item.")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
        return {"Data": "Not found"}
    

@app.post("/create-item/{item_id}")
async def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error" : "Item ID already exists"}
    
    inventory[item_id] = item
    return inventory[item_id]