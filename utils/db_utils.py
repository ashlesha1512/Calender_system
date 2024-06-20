from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

def create_session():
    DATABASE_URL = 'mysql+mysqlconnector://ashlesha.patil:vxcgsfuytssjalk@localhost/calendar_db'
    engine = create_engine(DATABASE_URL)
    session = sessionmaker(bind=engine)
    return session()