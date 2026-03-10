import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_error_status_code(client):
    response = client.get("/api/error")
    assert response.status_code == 500

def test_error_json(client):
    response = client.get("/api/error")
    assert response.get_json() == {"error": "Simulated failure"}
