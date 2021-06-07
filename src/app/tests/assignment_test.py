"""
Test cases for assignment api's
"""
import json

from src.app.api.assignment.v1.assignment_api import *


# client is a fixture, injected by the `pytest-flask` plugin
def test_get_assignment(client):
    """Test `assignments/<id>` api"""
    data = json.dumps(
        {
            "name": "assignment1",
            "title": "title1",
            "description": "desc1",
            "type": "t1",
            "duration": 90,
            "tags": [
                "GMAT", "SPACE"
            ]
        }
    )
    client.post('/assignments', data=data, content_type='application/json')

    response = client.get("/assignments/1")

    # Validate the response
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "name": "assignment1",
        "title": "title1",
        "description": "desc1",
        "type": "t1",
        "duration": 90,
        "tags": [
            "GMAT",
            "SPACE"
        ]
    }

    # response1 = client.get("/assignments/2")
    # assert response1.status_code != 200
