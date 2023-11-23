from app.database.db import session
from app.database.model import User
from flask_restful import Resource, reqparse
from app.auth.password import Password
from flask import json, request

# instantiate the parse method
parser = reqparse.RequestParser()

# get parsed response from form
parser.add_argument('firstname', type=str, location='form')
parser.add_argument('email', type=str,location='form')
parser.add_argument('password', type=str, location='form')

# create a user api class
class UserApi(Resource):
    
    # show a specific users
    def get(self, id=None):
        
        # get a paticular users from DB
        result = session.query(User).filter(User.id == id).first()
        # close the db connection
        session.close()
        res ={
            'name': result.fullname,
            'email': result.email
        }
        return res

    # add a users to the db
    def post(self):
        
        # get the parsed users param
        args = parser.parse_args()
        name = args['firstname']
        email = args['email']
        password = args['password']
        
        # hash the Password
        pswhash = Password.hash(password=password)
        
        # chwck if user already exit in the db
        user = session.query(User).filter(User.email == email).first()
        
        
        # check if user exist
        if user:
            return {'msg': 'Username already exist'}
        
        # add the necw user a to he DB
        new_user = User(fullname=name, email=email, password=pswhash)
        session.add(new_user)
        session.commit()
        session.close()
        res = {
            'name': name,
            'email': email
            }
        return json.dumps(res)
    

    def put(self, id):
        args = parser.parse_args()
        name = args['firstname']
        email = args['email']
        update_user = session.query(User).filter(User.id == id).first()
        
        if not update_user:
            return {'msg':'Invalid user'}
        
        user = User(fullname=name, email=email)
        session.add(user)
        session.commit()


    def delete(self, id):
        session.query(User).filter(User.id == id).delete()
        session.commit()
