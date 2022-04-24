from fastapi import Depends, Response, status as status_code
from fastapi.routing import APIRouter

from app.framework.injection import get_user_service
from app.user.model import User
from app.user.schema import CreateUserSchema, UpdateUserSchema
from app.user.service import UserService
from app.exception.model import HttpException

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get("/")
def get_users(username: str = None, status: User.Status = None, user_service: UserService = Depends(get_user_service)):
    return user_service.get_users(username, status)


@user_router.post("/", status_code=status_code.HTTP_201_CREATED)
def create_user(data: CreateUserSchema, response: Response, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.create_user(data)
    except HttpException as e:
        return e.get_response(response)


@user_router.get("/{user_id}")
def get_user(user_id: int, response: Response, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.get_user(user_id)
    except HttpException as e:
        return e.get_response(response)


@user_router.put("/{user_id}")
def update_user(user_id: int, data: UpdateUserSchema, response: Response,
                user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.update_user(user_id, data.dict(exclude={"confirm_password"}))
    except HttpException as e:
        return e.get_response(response)


@user_router.delete("/{user_id}")
def delete_user(user_id: int, response: Response, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.delete_user(user_id)
    except HttpException as e:
        return e.get_response(response)
