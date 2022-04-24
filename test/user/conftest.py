from typing import List

import pytest
from faker import Faker

from app.user.model import User
from app.user.schema import UserRepository


@pytest.fixture
def test_user_repository():
    class TestUserRepository(UserRepository):
        def exists_user(self, email: str, username: str) -> bool:
            return True

        def get_user(self, user_id: int) -> User:
            return User()

        def get_users(self, username: str = None,
                      status: User.Status = None,
                      skip: int = 0,
                      limit: int = 100) -> List[User]:
            return []

        def create_user(self, data):
            pass

        def update_user(self, user_id, data):
            pass

        def delete_user(self, user_id: int):
            pass
    return TestUserRepository()


@pytest.fixture
def user_valid():
    fake = Faker()
    return {
        "email": fake.name() + "@email.email",
        "username": fake.name(),
        "password": "password",
        "confirm_password": "password"
    }


@pytest.fixture
def user_wrong():
    return {
        "email": "email@email",
        "username": None,
        "password": "password",
        "confirm_password": "password1"
    }
