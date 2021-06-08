"""
Integrated tests for assignment api's. These operations are done on test database
"""

from app.api.assignment.v1.assignment_api import *


# client is a fixture, injected by the `pytest-flask` plugin
def test_create_assignment(client):
    """Create assignment"""
    data = json.dumps({"name": "assignment1", "title": "title1", "description": "desc1", "type": "t1", "duration": 90,
                       "tags": ["GMAT", "SPACE"]})
    resp = client.post('/assignments', data=data, content_type='application/json')
    assert resp.status_code == 201

    data1 = json.dumps({"name": "assignment2", "title": "title2", "description": "desc2", "type": "t2", "duration": 40,
                        "tags": ["GMAT", "GRE"]})
    resp1 = client.post('/assignments', data=data1, content_type='application/json')
    assert resp1.status_code == 201


def test_get_assignment_success(client):
    """test_get_assignment"""

    response = client.get("/assignment/1")

    # Validate the response
    assert response.status_code == 200
    assert response.json == {"id": 1, "name": "assignment1", "title": "title1", "description": "desc1", "type": "t1",
                             "duration": 90, "tags": ["GMAT", "SPACE"]}

    response1 = client.get("/assignment/2")
    assert response1.json == {"id": 2, "name": "assignment2", "title": "title2", "description": "desc2", "type": "t2",
                              "duration": 40, "tags": ["GMAT", "GRE"]}


def test_get_assignment_failure(client):
    """test_get_assignment"""
    response = client.get("/assignment/100")
    assert response.status_code == 400
    assert response.json == {'status': 'Could not retrieve assignment', 'status_code': 400}


def test_get_tags_success(client):
    """test_get_tags"""
    response = client.get("/assignments/" + '["GRE"]')
    assert response.json == [{"id": 2, "name": "assignment2", "title": "title2", "description": "desc2", "type": "t2",
                              "duration": 40, "tags": ["GMAT", "GRE"]}]
    assert response.status_code == 200


def test_get_tags_failure(client):
    """test_get_tags"""
    response = client.get("/assignments/" + '["GRE_DUMMY"]')
    assert response.json == []


def test_all_assignments(client):
    """Test all assignments"""
    response = client.get("/assignments")
    assert len(response.json) == 2
