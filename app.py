from flask import Flask, render_template, session, redirect
from functools import wraps
from database import db


app = Flask(__name__)
app.secret_key=b'\xbfrW\xb61\xa6i}n\xb7=S\x11\xc3m\xcd'

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

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

