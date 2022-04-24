from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from app.framework.database import init_db
from app.framework.route import include_routers


def create_app():
    app = FastAPI()

    include_routers(app)

    init_db(app)

    return app
