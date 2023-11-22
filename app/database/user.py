from app.database.db import session
from model import User
from flask_restful import Resource, reqparse

# instantiate the parse method
parser = reqparse.RequestParser()

# get parsed response from form
parser.add_argument('firstname', type=str)
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)

# create a user api class
class UserApi(Resource):
    
    # show a specific users
    def get(self, id=None):
        
        # get a paticular users from DB
        result = session.query(User).filter(User.id == id).first()
        # close the db connection
        session.close()
        return result

    # add a users to the db
    def post(self):
        
        # get the parsed users param
        args = parser.parse_args()
        name = args['firstname']
        email = args['email']
        password = args['password']
        
        # hash the Password
        
        
        # chwck if user already exit in the db
        user = session.query(User).filter(User.email == email).first()
        
        # check if user exist
        if user:
            return {'msg': 'Username already exist'}
        
        # add the necw user a to he DB
        new_user = User(name, email, password)
        session.add(new_user)
        session.commit()
        session.close()
    
    def put(self, id):
        args = parser.parse_args()
        name = args['firstname']
        email = args['email']
        update_user = session.query(User).filter(User.id == id).first()
        
        if not update_user:
            return {'msg':'Invalid user'}
        
        user = User(firstname=name, email=email)
        session.add(user)
        session.commit()


    def delete(self, id):
        session.query(User).filter(User.id == id).delete()
        session.commit()
