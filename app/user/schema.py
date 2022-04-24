from typing import List

from pydantic import BaseModel

from app.user.model import User


class UserRepository:
    def exists_user(self, email: str, username: str) -> bool:
        pass

    def get_user(self, user_id: int) -> User:
        pass

    def get_users(self, username: str = None,
                  status: User.Status = None,
                  skip: int = 0,
                  limit: int = 100) -> List[User]:
        pass

    def create_user(self, data):
        pass

    def update_user(self, user_id, data):
        pass

    def delete_user(self, user_id: int):
        pass


class CreateUserSchema(BaseModel):
    email: str
    username: str
    password: str
    confirm_password: str


class UpdateUserSchema(BaseModel):
    email: str
    username: str
    password: str
    confirm_password: str
