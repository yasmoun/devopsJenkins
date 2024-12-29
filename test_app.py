import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/')
    assert rv.data == b"Bienvenue à l'API de gestion des tâches!"
