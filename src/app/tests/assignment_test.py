from src.app.api.assignment.v1.assignment_api import *

# client is a fixture, injected by the `pytest-flask` plugin
def test_get_assignment(client):
    response = client.get("assignments/1")

    # Validate the response
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "name": "string",
        "title": "string",
        "description": "string",
        "type": "string",
        "duration": 0,
        "tags": [
            "a",
            "b"
        ]
    }
