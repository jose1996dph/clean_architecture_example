from typing import List

import pytest

from app.task.model import Task
from app.task.schema import TaskRepository


@pytest.fixture
def test_task_repository():
    class TestTestRepository(TaskRepository):
        def get_task(self, task_id: int) -> Task:
            return Task()

        def get_tasks(self,
                      description: str = None,
                      user_id: int = None,
                      skip: int = 0,
                      limit: int = 100) -> List[Task]:
            return [
                Task()
            ]

        def create_task(self, data):
            pass

        def update_task(self, task_id: int, data):
            pass

        def delete_task(self, task_id: int):
            pass
    return TestTestRepository()


@pytest.fixture
def task_valid():
    return {
        "title": "Title",
        "description": "Description",
        "user_id": 1,
    }


@pytest.fixture
def task_wrong():
    return {
        "title": None,
        "description": None,
        "user_id": None
    }
