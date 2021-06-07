"""Config"""

import os

# Load the development "mode". Use "development" if not specified
env = os.environ.get("PYTHON_ENV", "development")

# Configuration for each environment
# Alternatively use "python-dotenv"
all_environments = {
    "development": {"port": 5000, "debug": True, "swagger-url": "/api/swagger",
                    "SQLALCHEMY_DATABASE_URI": "sqlite:///db.sqlite", "SQLALCHEMY_TRACK_MODIFICATIONS": False},
    "production": {"port": 5000, "debug": False, "swagger-url": "/api/swagger",
                   "SQLALCHEMY_DATABASE_URI": "sqlite:///db.sqlite", "SQLALCHEMY_TRACK_MODIFICATIONS": False}
}

# The config for the current environment
environment_config = all_environments[env]
