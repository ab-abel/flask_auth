from flask import request
from app.database.db import session
from app.database.model import User
from app.auth.password import Password


class Registration:
    
    def __init__(self, fullname, email, password) -> None:     
        self.fullname = fullname
        self.email = email
        self.pwd = password
    
    
    def register_user(self):

        # add the user;
        pswhash = Password.hash(password=self.pwd)
        user = User(fullname = self.fullname, email=self.email, password=pswhash)
        session.add(user)
        session.commit()
        session.close()
        return {
            "msg":"User created successfully!"}
