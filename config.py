import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost/calendar_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config()


