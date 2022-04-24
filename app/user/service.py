from app.exception.model import HttpException
from app.user.model import User
from app.user.repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users(self, username: str = None, status: User.Status = None):
        return self.user_repository.get_users(username, status)

    def get_user(self, user_id: int):
        user = self.user_repository.get_user(user_id)

        if user is None:
            raise HttpException(HttpException.StatusCode.not_found, "User not found")

        return user

    def create_user(self, data: any):
        if self.user_repository.exists_user(data.email, data.username):
            raise HttpException(HttpException.StatusCode.unprocessable_entity, "User exists")

        return self.user_repository.create_user(data)

    def update_user(self, user_id: int, data: any):
        user = self.user_repository.get_user(user_id)

        if user is None:
            raise HttpException(HttpException.StatusCode.not_found, "User not found")

        return self.user_repository.update_user(user_id, data)

    def delete_user(self, user_id: int):
        user = self.user_repository.get_user(user_id)

        if user is None:
            raise HttpException(HttpException.StatusCode.not_found, "User not found")

        return self.user_repository.delete_user(user_id)
