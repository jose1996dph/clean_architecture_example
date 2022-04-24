from sqlalchemy import insert, func
from sqlalchemy.orm import Session
from .model import User
from .schema import UserRepository


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def exists_user(self, email: str, username: str):
        return self.db.query(User)\
                   .filter(func.lower(User.email) == email.lower() or User.username == username)\
                   .first() is not None

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_users(self, username: str = None, status: User.Status = None, skip: int = 0, limit: int = 100):
        query = self.db.query(User)

        if username is not None:
            query = query.filter(User.username.lower().like(username.lower()))

        if status is not None:
            query = query.filter(User.status == status)

        return query.offset(skip).limit(limit).all()

    def create_user(self, data):
        user = User(**data.dict(exclude={"confirm_password"}))
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user_id, data):
        query = self.db.query(User).where(User.id == user_id)
        query.update(data,  synchronize_session="fetch")
        return query.first()

    def delete_user(self, user_id: int):
        # query = self.db.query(User).filter(User.id == user_id).delete(synchronize_session="fetch")
        query = self.db.query(User).where(User.id == user_id)
        query.update({"status": User.Status.inactive}, synchronize_session="fetch")
        return query.first()
