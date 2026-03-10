import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_data_status_code(client):
    response = client.get("/api/data")
    assert response.status_code == 200

def test_data_length(client):
    response = client.get("/api/data")
    data = response.get_json()
    assert len(data["data"]) == 4
