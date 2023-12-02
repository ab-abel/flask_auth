from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import UserMixin

# initialize using SQLALchemy module
db = SQLAlchemy()


# create a table for class state
class User(db.Model, UserMixin):
    '''
        class defintion for SQL table states
        pARAMETER
            Base declarative
        Return:
        base meta data for the creation of state tables
    '''
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
     
    def __init__(self, fullname, email, password):
       self.fullname = fullname
       self.email = email
       self.password = password
   
    @property
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
