from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello from Zero Trust Container!"
    assert data["version"] == "1.0.0"
    assert "hostname" in data


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_generate_token():
    response = client.get("/token")
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert len(data["token"]) == 64  # secrets.token_hex(32) → 64자


def test_token_is_unique():
    response1 = client.get("/token")
    response2 = client.get("/token")
    assert response1.json()["token"] != response2.json()["token"]