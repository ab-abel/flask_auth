from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from app.database.db import create_db, session
from app.database.user import UserApi
from flask_restful import Api
from app.auth.register import Registration
from app.auth.validate import Validation
from app.database.model import User

# load evironmental files
load_dotenv()

# instantiate the main app
app = Flask(os.getenv('APP_NAME'),
            template_folder='templates',
            static_folder='static')

# load routes
# from core.routes import bp as main_bp
# app.register_blueprint(main_bp)

# use the rest API

api = Api(app)


api.add_resource(UserApi,
                 '/api/user/',
                 '/api/user/<int:id>'
                 )


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
            user = session.query(User).filter(User.email == email).first()
            if not user: 
                resgister_class = Registration(fullname, email, password)
                resgister_class.register_user()
                return render_template('home.html')
            else: 
                return {'msg': 'User already exist'}, render_template('register.html')
                        
    else:
        return render_template('register.html')


@app.route('/login', methods= ['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/')
def home():
    return render_template('/home.html')

# run the code
if __name__ == '__main__':
    app.run(debug=True)
    create_db()
    
 