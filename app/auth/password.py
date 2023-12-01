from werkzeug.security import generate_password_hash, check_password_hash

class Password:
    
    def hash(password:str):
        return generate_password_hash(password=password)
    
    def verify_password(self, pwdhash, password):
        return check_password_hash(pwhash=pwdhash, password=password)