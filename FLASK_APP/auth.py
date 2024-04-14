from flask import Flask, request, jsonify,Blueprint,make_response
from books_model import BooksModel
from functools import wraps
import jwt
import datetime
import json



SECRET_KEY = '****************************'

def login(data):
    user = data.get('username')
    pwd =  data.get('password')
    
    if user and pwd:
        token = genrate_token(user)
        return token
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

def genrate_token(username):
    """
    Takes username as input and genrates the token
    """
    data = {"username" : username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=1) }
    new_token = jwt.encode(data, SECRET_KEY, algorithm='HS256')
    return new_token.encode('utf-8')

#token Validation decorator
def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        new_token = request.headers.get('Authorization')
        if not new_token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(new_token, SECRET_KEY, algorithms=['HS256'])
            current_user = data['username']
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        return func(current_user=current_user, *args, **kwargs)
    return decorated



