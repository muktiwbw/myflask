from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from app import bcrypt, db
from app.setting.model import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    if not request.is_json:
        return jsonify({
            'message': 'Missing JSON in request'
        }), 400

    username = request.json.get('username')
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username has already been taken.'}), 400

    email = request.json.get('email')
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email has already been taken.'}), 400
    
    name = request.json.get('name')
    password = bcrypt.generate_password_hash(request.json.get('password')).decode('utf-8')

    user = User( \
        username=username, \
        email=email, \
        name=name, \
        password=password \
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': 'success',
        'data': {
            'username': user.username,
            'email': user.email,
            'name': user.name,
            'created_at': user.created_at
        }
    }), 201
    

@auth.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({
            'message': 'Missing JSON in request'
        }), 400

    user = User.query.filter_by(email=request.json.get('email')).first()

    if not (user and bcrypt.check_password_hash(user.password, request.json.get('password'))):
        return jsonify({'message': 'Incorrect username or password'}), 401

    access_token = create_access_token(identity=user.id)

    return jsonify({'access_token': access_token}), 200
