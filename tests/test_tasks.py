import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post(
        "/api/tasks",
        data={
            "title": "Test Task",
            "description": "Testing",
            "due_date": "2025-12-31",
            "status": "pending"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["status"] == "pending"

def test_get_tasks():
    response = client.get("/api/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
