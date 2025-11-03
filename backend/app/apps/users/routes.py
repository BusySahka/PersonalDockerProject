from fastapi import APIRouter, status

from apps.users.schemas import UserBaseFieldsSchema, RegisterUserSchema

users_router = APIRouter()


@users_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(user_data: RegisterUserSchema) -> UserBaseFieldsSchema:
    """create user based on name email password"""
    return user_data