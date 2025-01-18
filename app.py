from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson.objectid import ObjectId

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["items"]

@app.post("/items/")
async def create_item(name: str, description: str):
    item = {"name": name, "description": description}
    result = collection.insert_one(item)
    return {"id": str(result.inserted_id)}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return {"name": item["name"], "description": item["description"]}
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
async def update_item(item_id: str, name: str, description: str):
    result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": {"name": name, "description": description}})
    if result.matched_count:
        return {"status": "success"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count:
        return {"status": "success"}
    raise HTTPException(status_code=404, detail="Item not found")