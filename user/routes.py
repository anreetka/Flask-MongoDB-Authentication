from flask import Flask, render_template
from app import app
from itsdangerous import URLSafeSerializer, BadData
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
    return User().login()

@app.route('/user/forgot-password', methods=['POST'])
def forgot_user_password():
    return User().forgot_password()


@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    try:
        serializer = URLSafeSerializer(app.config['SECRET_KEY'])
        email = serializer.loads(token, salt='password-reset-salt', max_age=5)
    except BadData:
        return '<h1>The token is expired</h1>'
    return render_template('resetPassword.html', email=email)
