from fastapi import Depends
from fastapi.openapi.models import Response
from fastapi.routing import APIRouter

from app.exception.model import HttpException
from app.framework.injection import get_task_service
from app.task.service import TaskService
from app.task.schema import CreateTaskSchema, UpdateTaskSchema

task_router = APIRouter(prefix="/task", tags=["task"])


@task_router.get("/")
def get_tasks(description: str = None, user_id: int = None, skip: int = 0, limit: int = 100,
              task_service: TaskService = Depends(get_task_service)):
    return task_service.get_tasks(description, user_id, skip, limit)


@task_router.post("/")
def create_task(data: CreateTaskSchema, response: Response, task_service: TaskService = Depends(get_task_service)):
    try:
        return task_service.create_task(data)
    except HttpException as e:
        return e.get_response(response)


@task_router.get("/{task_id}")
def get_task(task_id: int, response: Response, task_service: TaskService = Depends(get_task_service)):
    try:
        return task_service.get_task(task_id)
    except HttpException as e:
        return e.get_response(response)


@task_router.put("/{task_id}")
def update_task(task_id: int, data: UpdateTaskSchema, response: Response, task_service: TaskService = Depends(get_task_service)):
    try:
        return task_service.update_task(task_id, data)
    except HttpException as e:
        return e.get_response(response)


@task_router.delete("/{task_id}")
def delete_task(task_id: int, response: Response, task_service: TaskService = Depends(get_task_service)):
    try:
        return task_service.delete_task(task_id)
    except HttpException as e:
        return e.get_response(response)
