import pytest
from app.app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello from GitHub Actions and Docker!" in response.data
