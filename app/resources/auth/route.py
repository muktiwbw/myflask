from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({
            'message': 'Missing JSON in request'
        }), 400

    if not (request.json.get('username') == 'muktiwbw' and request.json.get('password') == 'password'):
        return jsonify({
            'message': 'Incorrect username or password'
        }), 401

    access_token = create_access_token(identity='xx001')

    return jsonify({'access_token': access_token}), 200
