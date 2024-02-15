from flask import Flask, jsonify, request, session, redirect, url_for
from flask_mail import Mail, Message
from itsdangerous import URLSafeSerializer
from passlib.hash import pbkdf2_sha256
from database import db
from app import app
from app import mail
import uuid

class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        print(request.form)

        #Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name":request.form.get('name'),
            "email":request.form.get('email'),
            "password":request.form.get('password') 
        }
    
        #Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        if db.users.find_one({"email": user['email']}):
            return jsonify({"error":"Email address already in use!" }), 400       

        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400
    
    def signout(self):
        session.clear()
        return redirect('/')
    
    def login(self):

        user = db.users.find_one({
            "email": request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)
        
        return jsonify({"error": "Invalid error credentials"}), 401
    

    def forgot_password(self):
        user = db.users.find_one({
            "email": request.form.get('email')
        })

        if user:
           #code to send an email
            
            serializer = URLSafeSerializer(app.config['SECRET_KEY'])
            token = serializer.dumps(user['email'], salt='password-reset-salt')
            reset_url = url_for('reset_token', token=token, _external = True)
            msg = Message("Password Reset Request", sender="noreply@example.com", recipients=[user['email']])
            msg.body = f'''To reset your password, visit the following link:
            {reset_url}

            If you did not make this request, please ignore this email and no changes will be made'''

            mail.send(msg)
           
            return jsonify({"success": "Reset email sent!"}),200
        else:
            return jsonify({"error": "No registered account found with this email. Please create an account!"}), 401
        

    
      



