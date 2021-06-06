"""
#
"""
from flask_restplus import Resource
from src.server.wsgi import server
from .serializers import assignment_serializer
from src.models.assignment_model import Assignment
from flask import request
from src.models import db


@server.api.route('/assignments')
class AssignmentCreation(Resource):
    """ # """
    @server.api.marshal_list_with(assignment_serializer)
    def get(self):
        """

        :return:
        """
        assignments = Assignment.query.all()
        return assignments

    @server.api.response(201, 'Assignment successfully created')
    @server.api.expect(assignment_serializer)
    def post(self):
        """
        Create new assignment
        """
        data = request.json
        name = data.get('name', '')
        title = data.get('title', '')
        description = data.get('description', '')
        type = data.get('type', '')
        duration = data.get('duration', 0)
        tags = data.get('tags', [])
        assignment = Assignment(name, title, type, duration, description)
        assignment._set_tags(tags)
        assignment.save()
        return {"status": "ok"}, 201
