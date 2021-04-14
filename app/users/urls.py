from typing import Dict

from fastapi import APIRouter, Depends
from fastapi import status

from users.handlers import CreateUserHandler


router = APIRouter()


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=Dict
)
async def create_user(create: CreateUserHandler = Depends(CreateUserHandler)):
    result = await create()
    return result
