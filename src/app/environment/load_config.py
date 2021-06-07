"""Config"""

import os
import yaml


def read_config(env, filepath='app/environment/resources/configs.yaml'):
    """Load configuration based on environment"""
    with open(filepath, 'r') as f:
        return yaml.safe_load(f.read())[env]


# The config for the current environment
environment_config = read_config(os.environ.get("PYTHON_ENV", "development"))
