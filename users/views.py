from fastapi import APIRouter

from users.schemas import CreateUser
from users.crud import create_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_users(user: CreateUser):
    return create_user(user_in=user)