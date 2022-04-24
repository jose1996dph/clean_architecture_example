import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.framework.database import Base


class User(Base):
    class Status(enum.Enum):
        active = 1
        inactive = 2

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    status = Column(Enum(Status), default=Status.active)

    tasks = relationship("Task", back_populates="user")

    def is_active(self) -> bool:
        return self.status == User.Status.active
