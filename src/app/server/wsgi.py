"""
Initialize server instance
"""
from flask import Flask
from flask_restplus import Api
from app.models import db
from app.environment.config import environment_config


class Server(object):
    """server class is responsible for creating new flask application and to load required db configs"""
    def __init__(self):
        # Create flask application
        self.app = Flask(__name__)
        # Load sqlalchemy related configs
        self.app.config['SQLALCHEMY_DATABASE_URI'] = environment_config["SQLALCHEMY_DATABASE_URI"]
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = environment_config["SQLALCHEMY_TRACK_MODIFICATIONS"]
        # Create flask-restplus instance
        self.api = Api(self.app, title='Assignment API', doc=environment_config["swagger-url"])
        db.init_app(self.app)

    def run(self):
        """runner"""
        self.app.run(
            debug=environment_config["debug"],
            port=environment_config["port"],
            host='0.0.0.0'
        )


# Initialize server
server = Server()


@server.app.before_first_request
def create_tables():
    """This function makes the application to create all the tables before first request"""
    db.create_all()

