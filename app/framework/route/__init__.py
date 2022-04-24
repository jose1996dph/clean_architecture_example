from app.user.route import user_router
from app.task.route import task_router


def include_routers(app):
    app.include_router(user_router)
    app.include_router(task_router)
