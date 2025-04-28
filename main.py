from fastapi import FastAPI, Body, Path
from typing import Annotated

from pydantic import EmailStr, BaseModel
import uvicorn

from items_views import router as items_router
from users.views import router as users_router
from contextlib import asynccontextmanager
from core.models import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    
app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def hello_index():
    return {
        "message": "Hello index",
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)