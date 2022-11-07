from models.users import User
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()

def auth_register():
    try:
        user = User(
            email = request.json('email'),
            name = request.json('name'),
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf8'),
            age = request.json('age'),
            address = request.json('address'),
            city = request.json('city'),
            state = request.json('state'),
            country = request.json('country'),
        )
        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude = ['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'email is already in use, please use another'}, 409
        
