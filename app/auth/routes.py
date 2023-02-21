from flask import Blueprint, request, redirect, url_for, jsonify
from models import User
from .forms import UserCreationForm, LoginForm
from flask_login import login_user, logout_user, login_required
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth


auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signup', methods=["GET", "POST"])
def signUpPage():
    data=request.json
    print(request.method)
    if request.method == 'POST':
        print(data)
        first_name=data['first_name']
        last_name = data['last_name']
        email = data['email']
        password= data['password'] 
        
        print(first_name, last_name, email, password)

        # add user to database
        user = User(first_name, last_name, email, password)
        print(user)

        user.saveToDB()

            # return redirect(url_for('contactPage'))
        return 'ok'


    return 'hi'
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()



@basic_auth.verify_password
def verifyPassword(email, password):
    print(email, password)
    user = User.query.filter_by(email=email).first()
    if user:
        if user.password == password:
            return user

@token_auth.verify_token
def verifyToken(token):
    user = User.query.filter_by(apitoken=token).first()
    print(user, 'verify')
    if user:
        return user




@auth.route('/login', methods=["POST"])
@basic_auth.login_required
# Login Function
def getToken():
    user = basic_auth.current_user()
    if user:
        print(user)
        return {
            'status': 'ok',
            'user': user.to_dict()
        }
    else:
        return {
            'status': 'not ok'
        }, 400
# @auth.route('/login', methods=["GET", "POST"])
# def loginPage():
#     data=request.json

#     if request.method == "POST":
        
#             email = data['email']
#             password = data['password']

#             # check is user with that username even exists
#             user = User.query.filter_by(email=email).first()
#             if user:
#                 #if user ecxists, check if passwords match
#                 if user.password == password:
#                     login_user(user)
#                     return jsonify({'email': email, 'first_name': user.first_name})
#                 else:
#                     print('wrong password')
#                     return 'wrong password', 400

#             else:
#                 print('user doesnt exist')
#                 return 'no user found', 400



    

# @auth.route('/logout', methods=["GET"])
# @login_required
# def logoutRoute():
#     logout_user()
#     return redirect(url_for('loginPage'))