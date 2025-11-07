import pytest
from app.web_snake import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    r = client.get('/')
    assert r.status_code == 200
    assert b"Snake" in r.data

def test_state_and_move(client):
    move = client.post('/move', json={"dir": [1, 0]})
    assert move.status_code == 200
    state = client.get('/state').get_json()
    assert "snake" in state
    assert "food" in state
    assert "score" in state
