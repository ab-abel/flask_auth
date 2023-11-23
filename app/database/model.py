from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# define Base class for table class inheritance
Base = declarative_base()


# create a table for class state
class User(Base):
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
