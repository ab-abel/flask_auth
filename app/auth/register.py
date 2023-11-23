from flask import request
from app.database.db import session
from app.database.model import User
from app.auth.password import Password

class Registration():
    
    def __init__(self) -> None:     
        self.fullname = request.form['fullname']
        self.email = request.form['email']
        self.pwd =request.form['password']
    
    
    def register_user(self):
        
        pass
            
    def user_exist(email):
        user = session.query(User).filter(User.email == email).first()
        if not user:
            return {'msg':"User already exist"}
        
