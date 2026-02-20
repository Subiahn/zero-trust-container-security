# tests/test_app.py
import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello from Zero Trust Container' in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_get_user(client):
    response = client.get('/user/testuser')
    assert response.status_code == 200

def test_generate_token(client):
    response = client.get('/token')
    assert response.status_code == 200
    data = response.get_json()
    assert 'token' in data
    assert len(data['token']) == 64  # secrets.token_hex(32) = 64자