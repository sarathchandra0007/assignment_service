"""
#
"""
from flask_restplus import Resource
from src.server.wsgi import server
from .serializers import assignment_serializer
from src.models.assignment_model import Assignment, Tag
from flask import request
from src.models import db

@server.api.route('/assignments')
class AssignmentCollection(Resource):
    """ AssignmentCollection """

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


@server.api.route('/assignments/<int:id>')
class AssignmentInfo(Resource):
    """AssignmentInfo"""

    @server.api.marshal_list_with(assignment_serializer)
    def get(self, id):
        assignment = Assignment.query.filter(Assignment.id == id).first()
        return assignment


@server.api.route('/assignments/<tags>')
class AssignmentTag(Resource):
    """AssignmentTag"""

    @server.api.marshal_list_with(assignment_serializer)
    def get(self, tags):
        q = db.session.query(Assignment)
        tags = list(tags.split(","))
        resp = q.filter(Assignment.tags.any(Tag.name.in_(tags))).all()
        return resp
