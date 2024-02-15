from flask import Flask, render_template, session, redirect
<<<<<<< HEAD
from functools import wraps
from database import db


app = Flask(__name__)
app.secret_key=b'\xbfrW\xb61\xa6i}n\xb7=S\x11\xc3m\xcd'
=======
from flask_mail import Mail, Message
from functools import wraps
from database import db
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xbfrW\xb61\xa6i}n\xb7=S\x11\xc3m\xcd'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS']= True
app.config['MAIL_USERNAME'] = 'anreetkaur04@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')
mail = Mail(app)
>>>>>>> new_branch

#Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
        
    return wrap

#Routes
from user import routes
@app.route('/')
def home():
    return render_template('home.html')

<<<<<<< HEAD
=======
@app.route('/forgot-password')
def forgot_password():
    return render_template('forgotPassword.html')

>>>>>>> new_branch
@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

<<<<<<< HEAD
=======

>>>>>>> new_branch
if __name__ == '__main__':
    app.run(debug=True)

