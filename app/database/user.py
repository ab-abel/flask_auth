from app.database.db import session
from model import User

def create(data):
    users = 

def view():
    pass

def show(id):
    result = session.query(User).filter(User.id == id).first()
    session.close()
    return result

def update(id):
    pass

def delete(id):
    session.query(User).filter(User.id == id).delete()
    session.commit()
