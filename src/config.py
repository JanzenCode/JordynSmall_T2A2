import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Database Connection (SQLALCHEMY + PSYCHOG2)
SQLALCHEMY_DATABASE_URI = 'your psycopg2 URI connection'

# Turn off the Flask-SQLAlchemy 
SQLALCHEMY_TRACK_MODIFICATIONS = False