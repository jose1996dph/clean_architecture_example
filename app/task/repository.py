from typing import List

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.task.model import Task
from app.task.schema import TaskRepository


class SqlAlchemyTaskRepository(TaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_task(self, task_id: int) -> Task:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def get_tasks(self, description: str = None, user_id: int = None, skip: int = 0, limit: int = 100) -> List[Task]:
        query = self.db.query(Task)

        if user_id is not None:
            query = query.filter(Task.user_id == user_id)

        if description is not None:
            query = query.where(Task.description.like(f"%{description}%") or Task.title.like(f"%{description}%"))

        return query.offset(skip).limit(limit).all()

    def create_task(self, data):
        task = Task(**data)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task(self, task_id: int, data):
        query = self.db.query(Task).where(Task.id == task_id).update(data,  synchronize_session="fetch")
        return self.db.execute(query)

    def delete_task(self, task_id: int):
        query = self.db.query(Task).filter(Task.id == task_id).delete(synchronize_session="fetch")
        return self.db.execute(query)
