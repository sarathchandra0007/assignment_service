"""
Conf test
"""
import pytest
from app.server.wsgi import server


# This implicitly creates the `client` fixture, which allows us to execute test API calls.
@pytest.fixture(scope='session')
def app():
    """Creates a fixture whose name is "app" and returns our flask server instance."""
    app = server.app
    # Create an in memory database to run tests
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    return app
