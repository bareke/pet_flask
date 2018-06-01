import os

BASE_DIR = os.getcwd()

# Config of the app

class BaseConfig():
    """
    Config basic app
    """
    UPLOAD_FOLDER = 'static/pet_images'
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
    SECRET_KEY = 'est0-es_una-clav3-criptografic@'
    DATABASE =  BASE_DIR + '/db.sqlite3'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + DATABASE
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_IMAGES_DEST = BASE_DIR + '/app/static/profile_img/'
    UPLOADED_IMAGES_URL = 'http://localhost:5000/static/profile_img/'


class DevelopmentConfig(BaseConfig):
    """
    Config development app
    """
    DEBUG = True


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    """
    Config testing app
    """
    TESTING = True
    DEBUG = False
