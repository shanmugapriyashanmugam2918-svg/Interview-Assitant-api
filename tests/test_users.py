from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)
email = f"{uuid.uuid4()}@test.com"
username = f"{uuid.uuid4()}"


def test_application_loads():
    assert app is not None


def test_register_load():
    response = client.post(
        "/users/register",
        json={"username": username, "email": email, "password": "pwd123"},
    )
    assert response.status_code == 200


def test_login_load():
    response = client.post(
        "/users/login", json={"email": email, "pwd": "pwd123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
