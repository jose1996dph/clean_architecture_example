from dataclasses import dataclass
from typing import List

from pydantic import BaseModel

from app.task.model import Task


class TaskRepository:
    def get_task(self, task_id: int) -> Task:
        pass

    def get_tasks(self, description: str = None, user_id: int = None, skip: int = 0, limit: int = 100) -> List[Task]:
        pass

    def create_task(self, data):
        pass

    def update_task(self, task_id: int, data):
        pass

    def delete_task(self, task_id: int):
        pass


@dataclass
class CreateTaskSchema:
    title: str
    description: str
    user_id: int


@dataclass
class UpdateTaskSchema(BaseModel):
    title: str
    description: str
    user_id: int
