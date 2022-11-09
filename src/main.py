from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)
    db.init_(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    return app

