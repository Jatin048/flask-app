import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage_loads(client):
    response = client.get("/")
    assert response.status_code == 200

def test_homepage_content(client):
    response = client.get("/")
    assert b"Application Running Successfully" in response.data

def test_invalid_route(client):
    response = client.get("/invalid")
    assert response.status_code == 404
