"""
Assignment Api's
"""
import json

from flask_restplus import Resource
from app.server.wsgi import server
from app.api.assignment.v1.serializers import assignment_serializer, assignment_schema
from app.models.assignment_model import Assignment, Tag
from flask import request, jsonify
from app.models import db


@server.ns.route('/assignments')
class AssignmentCollection(Resource):
    """ AssignmentCollection is responsible to get all assignments and create an assignment"""

    @server.api.marshal_list_with(assignment_serializer)
    def get(self):
        """Get all assignments"""
        assignments = Assignment.query.all()
        return assignments

    @server.api.response(201, 'Assignment successfully created')
    @server.api.expect(assignment_serializer)
    def post(self):
        """Create new assignment"""
        data = request.json
        tags = data.get('tags', [])
        assignment = Assignment(
            name=data.get('name', ''),
            title=data.get('title', ''),
            description=data.get('description', ''),
            type=data.get('type', ''),
            duration=data.get('duration', 0)
        )
        assignment._set_tags(tags)
        assignment.save()
        return {"status": "ok"}, 201


@server.ns.route('/assignments/<int:id>')
class AssignmentInfo(Resource):
    """AssignmentInfo is responsible to get information of particular assignment"""

    @server.api.doc(responses={200: 'OK', 400: 'Invalid Id'},
                    params={'id': 'Specify the Id of assignment'})
    def get(self, id):
        """Get assignment info based on id"""
        assignment = Assignment.query.filter(Assignment.id == id).first()
        if assignment:
            result = assignment_schema.dump(assignment)
            return jsonify(result)
        else:
            server.api.abort(400, status='Could not retrieve assignment', status_code=400)


@server.ns.route('/assignments/<tags>')
class AssignmentTag(Resource):
    """AssignmentTag is responsible to return all assignments for a given tags"""

    @server.api.doc(responses={200: 'OK'})
    @server.api.marshal_list_with(assignment_serializer)
    def get(self, tags):
        """Get assignment info for given tags"""
        q = db.session.query(Assignment)
        tags = json.loads(tags)
        resp = q.filter(Assignment.tags.any(Tag.name.in_(tags))).all()
        return resp
