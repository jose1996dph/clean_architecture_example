from app.task.model import Task
from app.task.service import TaskService


def test_task_service(test_task_repository, test_user_repository):
    task_service: TaskService = TaskService(test_task_repository, test_user_repository)

    task = task_service.get_task(1)
    tasks = task_service.get_tasks("name", Task.Status.active)

    assert isinstance(task, Task)
    assert len(tasks) == 0


def test_valid_get_task(client, task_valid):
    created_response = client.post("/task/", json=task_valid)
    data = created_response.json()

    response = client.get(f"/task/{data['id']}")

    assert response.status_code == 200


def test_valid_create_task(client, task_valid):
    response = client.post("/task/", json=task_valid)
    assert response.status_code == 201


def test_wrong_create_task(client, task_wrong):
    response = client.post("/task/", json=task_wrong)
    assert response.status_code == 422


def test_valid_get_tasks(client):
    response = client.get("/task/")
    assert response.status_code == 200


def test_valid_update_task(client, task_valid):
    created_response = client.post("/task/", json=task_valid)
    data = created_response.json()
    task_valid['taskname'] = "otherTaskname"

    response = client.put(f"/task/{data['id']}", json=task_valid)

    assert response.status_code == 200
    assert response.json()['taskname'] == task_valid['taskname']


def test_wrong_update_task(client, task_wrong):
    response = client.put(f"/task/0", json=task_wrong)
    assert response.status_code == 422


def test_valid_delete_task(client, task_valid):
    created_response = client.post("/task/", json=task_valid)
    data = created_response.json()

    response = client.delete(f"/task/{data['id']}")

    assert response.status_code == 200


def test_wrong_delete_task(client):
    response = client.delete("/task/0")
    assert response.status_code == 404
