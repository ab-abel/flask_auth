'''
This module use the class created from ORM lesson
'''
# Import Modules from ORM
from sqlalchemy import Column, Integer, String, MetaData, Table

# create meta data from database schema
meta = MetaData()
user = Table('users', meta,
                  Column('id', Integer, primary_key=True,
                         autoincrement=True,
                         unique=True, nullable=False),
                  Column('fullname', String,
                         nullable=False),
                  Column('email', String,
                         nullable=False),
                  Column('password', String,
                         nullable=False)
                  )
