"""coding=utf-8."""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.framework.setting import Setting

database_url = Setting().database_url

engine = create_engine(database_url, echo=True)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db(app):
    @app.on_event("startup")
    def startup():
        from app.user.model import User
        from app.task.model import Task

        Base.metadata.create_all(engine)
