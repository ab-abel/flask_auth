from flask import Flask, render_template, request, url_for, redirect
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
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length
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


@app.route('/register', methods= ['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['firstname']
        email = request.form['email']
        password = request.form['password']
        validate = Validation()
        if not validate.is_empty(email) and \
            not validate.is_empty(password) and \
                not validate.is_empty(fullname) and \
                    validate.validate_email(email):
            user = User.query.filter_by(email= email).first()
            if not user: 
                user = User(fullname=fullname, email=email, password=password)
                db.session.add(user)
                db.session.commit()
                flash("Users added succesfully")
                return redirect(url_for('login'))
            else:
                if current_user.is_authenticated or not current_user.is_anonymous:
                    return redirect(url_for('profile'))
                return render_template('auth.register.html')
                        
    else:
        if current_user.is_authenticated or not current_user.is_anonymous:
            return redirect(url_for('profile'))
        return render_template('auth.register.html')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=120)])
#     remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
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
                return redirect(url_for("profile"))

    return render_template("login.html", form=form)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username = current_user)

@app.route('/logout')
@login_required
def logout():
    # logout_user()
    return redirect(url_for('home'))

# run the code
if __name__ == '__main__':
    app.run(debug=True)
    create_db()
