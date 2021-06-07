"""
Conf test
"""
import pytest
from app.server.wsgi import server


# This implicitly creates the `client` fixture, which allows us to execute test API calls.
@pytest.fixture
def app():
    """Creates a fixture whose name is "app" and returns our flask server instance."""
    app = server.app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite.test'
    return app
