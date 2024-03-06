from fastapi import FastAPI, Path

app = FastAPI()


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you would like to view")):
    return inventory[item_id]

#@app.post("/post-items/{item_id}")
#def post_item(item_id: int):
#    return inventory[item_id]