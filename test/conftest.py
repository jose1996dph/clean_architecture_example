import pytest as pytest
from dotenv import load_dotenv
from starlette.testclient import TestClient
from app import create_app


def pytest_generate_tests():
    load_dotenv()


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return TestClient(app)
