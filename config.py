import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecret')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_ECHO = True
    #UPLOAD_FOLDER = 'static/uploads'
    #ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    CSRF_TOKEN_TIMEOUT = 7200  
