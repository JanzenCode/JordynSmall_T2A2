from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, foreign_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(30))

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'name', 'age', 'address', 'city', 'state', 'country')