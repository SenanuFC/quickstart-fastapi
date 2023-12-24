from fastapi import FastAPI
from .routers import users

from enum import Enum

class usertype(str, Enum):
    staff = 'staff'
    manager = 'manager'
    admin = 'admin'


app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

@app.get("/user_type/{user_type}")
async def user_type(user_type: usertype):
    return {"user_type": user_type}