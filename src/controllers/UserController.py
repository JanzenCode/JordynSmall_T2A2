from flask import Blueprint
from init import db, ma, bcrypt, jwt
from sqlalchemy.exc import IntegrityError
from models.users import User

users_bp = Blueprint('users',__name__, url_prefix='/auth')

@users_bp.route('/register/ ')
def auth_register():
    try:
        user = User(
            email = request.json('email'),
            name = request.json('name'),
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
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
        
