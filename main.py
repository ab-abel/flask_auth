from flask import Flask, render_template
import os
from dotenv import load_dotenv
from app.database.db import create_db
from app.database.user import UserApi
from flask_restful import Api


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
    
 