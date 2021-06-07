"""Assignment serializer"""

from app.server.wsgi import server
from flask_restplus import fields

assignment_serializer = server.api.model('Assignment', {
    'id': fields.Integer(readonly=True, required=True, description='Unique identifier for an assignment'),
    'name': fields.String(required=True, description='Assignment name'),
    'title': fields.String(required=True, description='Assignment title'),
    'description': fields.String(description='Assignment description'),
    'type': fields.String(required=True, description='Assignment type'),
    'duration': fields.Integer(required=True, description='Assignment duration'),
    'tags': fields.List(fields.String, required=True, description='Assignment tags')
})
