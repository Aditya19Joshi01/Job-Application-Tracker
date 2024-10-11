import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_to_guess_string'
    
    # MySQL connection string format
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:aditya%40123%21@localhost/job_tracker_db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
