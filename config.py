import os

# Config of the app

class BaseConfig():
    pass

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'est0-es_una-clav3-criptografic@'
    WTF_CSRF_ENABLED = False
    DATABASE =  '{}/database.db'.format(os.getcwd())
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
