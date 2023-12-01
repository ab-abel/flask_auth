from flask import Flask, render_template, request, url_for, redirect

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
            user = db_session.query(User).filter(User.email == email).first()
            if not user: 
                resgister_class = Registration(fullname, email, password)
                resgister_class.register_user()
                return render_template('home.html')
            else: 
                return render_template('register.html')
                        
    else:
        return render_template('register.html')


@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        validate = Validation()
        if not validate.is_empty(email) and \
            not validate.is_empty(password) and \
                    validate.validate_email(email):
            user = db_session.query(User).filter(User.email == email).first()
            pwd = Password()
            # print(Password().verify_password(user.password, password))
            if user and pwd.verify_password(user.password, password):
                User().is_authenticated = True
                load_user(user_id=user.id)
                login_user(user=user, remember=True)
                return redirect(url_for('profile'))
        else:
            # return render_template('login.html')
            pass
    else:
        # return render_template('login.html')
        pass

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
