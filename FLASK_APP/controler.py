from app import app
from books_model import BooksModel
from auth import login,token_required
import json
from flask import request
obj = BooksModel()


app.config['SECRET_KEY'] = 'h8YtrfgeDWjvFre34rEtfZSqXfrT43Az'


auth_token = "z1CGYob0qcOKDsuAWumHRE"
def check_auth_token(func):
    from flask import make_response, jsonify,request
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token and token == auth_token:
            return func(*args, **kwargs)
        else:
            return jsonify({'message': 'Unauthorized'})
    return wrapper


@app.route("/books/getall")
@token_required
def get_books_info(current_user):
    return obj.get_books_data(current_user)

@app.route("/create_books",methods=['POST'])
@token_required
def create_books(current_user):
    if request.method == 'POST':
        books_data = request.json
        books_data = books_data['data']
        return obj.create_books(books_data)
    

@app.route("/update/<id>",methods=['PUT'])
@token_required
def update_user(id,current_user):
    if request.method == 'PUT':
        books_data = request.json
        books_data = books_data['data']
        return obj.update_data(books_data,id)
    

@app.route("/delete/<id>",methods=['DELETE'])
@token_required
def delete_user(id,current_user):
    if request.method == 'DELETE':
        return obj.delete_data(id)
    
@app.route("/login",methods=['POST'])
def login_user():
    auth_data = request.json
    data = auth_data.get('data')
    return login(data)


