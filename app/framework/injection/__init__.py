from functools import lru_cache

from fastapi import Depends
from sqlalchemy.orm import Session

from app.framework.setting import Setting
from app.task.repository import TaskRepository, SqlAlchemyTaskRepository
from app.task.service import TaskService
from app.user.repository import UserRepository, SqlAlchemyUserRepository
from app.user.service import UserService
from app.framework.database import session_local


@lru_cache()
def get_setting():
    return Setting()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


def get_user_repository(session: Session = Depends(get_db)):
    return SqlAlchemyUserRepository(session)


def get_user_service(user_repository: UserRepository = Depends(get_user_repository)):
    return UserService(user_repository)


def get_task_repository(session: Session = Depends(get_db)):
    return SqlAlchemyTaskRepository(session)


def get_task_service(task_repository: TaskRepository = Depends(get_task_repository),
                     user_repository: UserRepository = Depends(get_user_repository)):
    return TaskService(task_repository, user_repository)
