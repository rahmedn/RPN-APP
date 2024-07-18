from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_stack():
    response = client.post("/rpn/stack")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Stack created"
    assert "stack_id" in data


def test_get_stack():
    response = client.post("/rpn/stack")
    stack_id = response.json()["stack_id"]
    response = client.get(f"/rpn/stack/{stack_id}")
    assert response.status_code == 200
    assert response.json() == {"stack": []}


def test_clear_stack():
    response = client.post("/rpn/stack")
    stack_id = response.json()["stack_id"]
    response = client.delete(f"/rpn/stack/{stack_id}")
    assert response.json() == {"message": "Stack cleared"}


