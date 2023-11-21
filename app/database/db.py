from app.database.schema import meta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sqlalchemy
import os
from dotenv import load_dotenv

load_dotenv()

def create_db():
    try:
        engine = create_engine(os.getenv('DB_ENGINE'))
        meta.create_all(engine)
        
        Session = sessionmaker(bind=engine)
        
        session = Session()
        
        return session
    except AttributeError as e:
        print(f"error message {e}")

    except sqlalchemy.exc.ProgrammingError as e:
        print(f"An Error occured: {e}")

session = create_db()
