import pytest
from flask import url_for
from app import app, socketio

@pytest.fixture
def client():
    """
    Фикстура для создания тестового клиента Flask.
    """
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture
def socket_client(client):
    """
    Фикстура для создания тестового клиента SocketIO.
    """
    socket_client = socketio.test_client(app)
    yield socket_client
    socket_client.disconnect()

def test_socketio_connect(socket_client):
    assert socket_client.is_connected() is True

