from flask import render_template, request, redirect, url_for, flash, Blueprint
from ...forms import UserCreationForm, loginform, ItemSubmitForm
from ...models import User
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
# from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

# Aut Api#
api = Blueprint
@api.route('/api/signup', methods=["POST"])
def signUpPageApi():
    data=request.json 
    
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    password =data['password']

    # add user to database
    user = User(first_name, last_name, email, password)
    user.saveToDB()

    # return render_template('signup.html', form = form )
    return{
        'Status': 'ok',
        'message': 'You have successfully create an account'
        
    }
    # return redirect(url_for('loginPage'))


    


    