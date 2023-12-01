from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import UserMixin

# initialize using SQLALchemy module
db = SQLAlchemy()


# create a table for class state
class User(Base, UserMixin):
    '''
        class defintion for SQL table states
        pARAMETER
            Base declarative
        Return:
        base meta data for the creation of state tables
    '''
    # define table name
    __tablename__ = 'users'
    # define column for users
    id = Column(Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    fullname = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
