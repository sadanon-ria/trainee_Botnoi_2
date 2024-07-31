from fastapi import APIRouter
from model.models import User
from config.db import collection_line, collection_account

user = APIRouter()

@user.post("/post", tags=["user"])
async def post_users(user: User):
    collection_line.insert_one(dict(user))
    return {"status": "OK"}

@user.get("/finduser/{id}", tags=["user"])
async def get_one_user(id: str):
    user = collection_account.find_one({"sub": id}, {'_id': False})
    return {"status": "OK", "data":user}