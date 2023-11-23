from flask import request
from app.database.db import session
from app.database.model import User
from app.auth.password import Password



class Registration:
    
    def __init__(self, fullname, email, password) -> None:     
        self.fullname = fullname
        self.email = email
        self.pwd = password
    
    
    def login_user(self):
        pass