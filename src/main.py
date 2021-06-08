"""
Main file
"""
# Need to import all resources so that they register with the server
from app.api.assignment.v1.assignment_api import *

if __name__ == '__main__':
    server.run()
