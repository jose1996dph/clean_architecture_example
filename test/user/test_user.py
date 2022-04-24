import json

from app.user.model import User
from app.user.service import UserService


def test_user_service(test_user_repository):
    user_service: UserService = UserService(test_user_repository)

    user = user_service.get_user(1)
    users = user_service.get_users("name", User.Status.active)

    assert isinstance(user, User)
    assert len(users) == 0


def test_valid_get_user(client, user_valid):
    created_response = client.post("/user/", json=user_valid)
    data = created_response.json()

    response = client.get(f"/user/{data['id']}")

    assert response.status_code == 200


def test_wrong_get_user(client):
    response = client.get(f"/user/{0}")
    assert response.status_code == 404


def test_valid_create_user(client, user_valid: dict):
    response = client.post("/user/", json=user_valid)
    assert response.status_code == 201


def test_wrong_create_user(client, user_wrong):
    response = client.post("/user/", json=user_wrong)
    assert response.status_code == 422


def test_valid_get_users(client):
    response = client.get("/user/")
    assert response.status_code == 200


def test_valid_update_user(client, user_valid):
    created_response = client.post("/user/", json=user_valid)
    data = created_response.json()
    user_valid['username'] = "otherUsername"

    response = client.put(f"/user/{data['id']}", json=user_valid)

    assert response.status_code == 200
    assert response.json()['username'] == user_valid['username']


def test_wrong_update_user(client, user_wrong):
    response = client.put(f"/user/0", json=user_wrong)
    assert response.status_code == 422


def test_valid_delete_user(client, user_valid):
    created_response = client.post("/user/", json=user_valid)
    data = created_response.json()

    response = client.delete(f"/user/{data['id']}")

    assert response.status_code == 200


def test_wrong_delete_user(client):
    response = client.delete("/user/0")
    assert response.status_code == 404
