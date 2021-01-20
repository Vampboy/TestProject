import pytest

from runner import app

@pytest.fixture(scope="module")
def client():
    return app.test_client()
