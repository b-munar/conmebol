import pytest


from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_request_ping(client):
    response = client.get("/conmebol/ping")
    assert response.status_code == 200
    assert b"pong" in response.data
