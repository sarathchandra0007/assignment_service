"""
#
"""
from flask import Flask
from flask_restplus import Api
from src.models import db
from src.environment.config import environment_config


class Server(object):
    """server"""
    def __init__(self):
        self.app = Flask(__name__)
        # Load sqlalchemy related configs
        self.app.config['SQLALCHEMY_DATABASE_URI'] = environment_config["SQLALCHEMY_DATABASE_URI"]
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = environment_config["SQLALCHEMY_TRACK_MODIFICATIONS"]
        self.api = Api(self.app, title='Assignment API', doc=environment_config["swagger-url"])
        db.init_app(self.app)

    def run(self):
        """runner"""
        self.app.run(
            debug=environment_config["debug"],
            port=environment_config["port"]
        )


server = Server()


@server.app.before_first_request
def create_tables():
    """This function makes the application to create all the tables before first request"""
    db.create_all()

