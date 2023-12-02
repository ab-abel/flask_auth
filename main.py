from flask import Flask, render_template, request, url_for, redirect, flash
from app.auth.validate import Validation

# import for dot env load
import os
from dotenv import load_dotenv

# db annd User model import
from app.models.users_model import User
from app.models.users_model import db

# flask login import
from flask_login import current_user, login_user, login_required, logout_user, LoginManager

# flask form import
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, InputRequired, EqualTo
from flask_bootstrap import Bootstrap5

# for password hash
from werkzeug.security import generate_password_hash, check_password_hash

# load evironmental files
load_dotenv()

# instantiate the main app
app = Flask(os.getenv('APP_NAME'),
            template_folder='templates',
            static_folder='static')

# config secret and DB engine
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_ENGINE')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# intitize boostrap for form loader
bootstrap = Bootstrap5(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

class RegisterForm(FlaskForm):
    fullname = StringField('Fullname', [InputRequired()])
    email = EmailField('Email', [InputRequired()])
    password  = PasswordField('Password', [
        InputRequired(), EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password', [InputRequired()])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=120)])
#     remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

@app.route('/register', methods= ['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            fullname = request.form.get('fullname')
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email= email).first()
            if user:
                flash("Email already exist")
                return render_template('auth/register.html', form=form)
            user = User(fullname=fullname, email=email, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            flash("Users added succesfully")
            return redirect(url_for('login'))
        if form.errors:
            flash(form.errors, 'danger')
    
    if current_user.is_authenticated or not current_user.is_anonymous:
        return redirect(url_for('profile'))
    else: return render_template('auth/register.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    """For GET requests, display the login form. 
    For POSTS, login the current user by processing the form.
    """
#     print db
    if current_user.is_authenticated or not current_user.is_anonymous:
        return redirect(url_for('profile'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email= form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                # user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                flash('login successful')
                return redirect(url_for("profile"))
            else:
                flash('Invalid Password')
        else:
            flash('User does not exist')
    return render_template("auth/login.html", form=form)

@app.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html', username = current_user.fullname)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    # logout_user()
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('home'))

# run the code
if __name__ == '__main__':
       db.init_app(app)
       with app.app_context():
              db.create_all()
            #   db.drop_all()
       app.run(debug = True)
