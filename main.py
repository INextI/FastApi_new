from fastapi import FastAPI, Body, Path
from typing import Annotated

from pydantic import EmailStr, BaseModel
import uvicorn

from items_views import router as items_router


app = FastAPI()
app.include_router(items_router)
class CreateUser(BaseModel):
    email : EmailStr

@app.get("/")
def hello_index():
    return {
        "message": "Hello index",
    }


@app.post("/users")
def create_users(user: CreateUser):
    return {
        "message" : "success",
        "email" : user.email
    }

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)