import os

# Config of the app

class BaseConfig():
    UPLOAD_FOLDER = 'static/pet_images'
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'est0-es_una-clav3-criptografic@'
    WTF_CSRF_ENABLED = False
    DATABASE =  os.getcwd() + '/db.sqlite3'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
