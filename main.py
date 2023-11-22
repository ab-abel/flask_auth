from flask import Flask
import os
from dotenv import load_dotenv
from app.database.db import create_db
from app.database.user import UserApi


# load evironmental files
load_dotenv()

# instantiate the main app
app = Flask(os.getenv('APP_NAME'),
            template_folder='app/templates',
            static_folder='app/static')

# load routes
# from core.routes import bp as main_bp
# app.register_blueprint(main_bp)

# use the rest API




# run the code
if __name__ == '__main__':
    app.run(debug=True)
    create_db()
    
 