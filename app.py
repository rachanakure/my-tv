from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash('Sign in successful!', 'success')
            return redirect(url_for('profile.html'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('signin.html')

 

@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')


@app.route('/homepage', methods=['GET'])
def homepage():
    return render_template('homepage.html')

@app.route('/tvshows', methods=['GET'])
def tvshows():
    return render_template('tvshows.html')

@app.route('/mylist1', methods=['GET'])
def mylist1():
    return render_template('mylist1.html')    

@app.route('/popular1', methods=['GET'])
def popular1():
    return render_template('popular1.html')

if __name__ == '__main__':
    app.run(debug=True)
