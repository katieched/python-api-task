import pytest
import app
from controllers import dad_jokes

@pytest.fixture
def api(monkeypatch):
    test_dad_jokes = [
        {'id': 1, 'joke': 'test joke 1', 'punchline': "test punchline 1"},
        {'id': 2, 'joke': 'test joke 2', 'punchline': "test punchline 2"}
    ]
    monkeypatch.setattr(dad_jokes, "dad_jokes", test_dad_jokes)
    api = app.app.test_client()
    return api