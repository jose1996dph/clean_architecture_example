from app.exception.model import HttpException
from app.task.repository import TaskRepository
from app.user.repository import UserRepository


class TaskService:
    def __init__(self, task_repository: TaskRepository, user_repository: UserRepository):
        self.task_repository = task_repository
        self.user_repository = user_repository

    def get_task(self, task_id: int):
        task = self.task_repository.get_task(task_id)

        if task is None:
            raise HttpException(HttpException.StatusCode.not_found, "Task not found")

        return task

    def get_tasks(self, description: str = None, user_id: int = None, skip: int = 0, limit: int = 100):
        return self.task_repository.get_tasks(description, user_id, skip, limit)

    def create_task(self, data):
        user = self.user_repository.get_user(data.user_id)

        if user is None:
            raise HttpException(HttpException.StatusCode.unprocessable_entity, "User not found")

        if not user.is_active():
            raise HttpException(HttpException.StatusCode.unprocessable_entity, "User not found")

        return self.task_repository.create_task(data)

    def update_task(self, task_id: int, data):
        task = self.task_repository.get_task(task_id)

        if task is None:
            raise HttpException(HttpException.StatusCode.not_found, "Task not found")

        return self.task_repository.update_task(task_id, data)

    def delete_task(self, task_id: int):
        task = self.task_repository.get_task(task_id)

        if task is None:
            raise HttpException(HttpException.StatusCode.not_found, "Task not found")

        return self.task_repository.delete_task(task_id)
