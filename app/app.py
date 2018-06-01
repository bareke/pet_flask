from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_uploads import UploadSet
from flask_uploads import IMAGES
from flask_uploads import configure_uploads

from .config import DevelopmentConfig
from .config import TestingConfig

db = SQLAlchemy()
csrf = CSRFProtect()
images = UploadSet('images', IMAGES)

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())

    # Init database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Init CRSF Protect
    csrf.init_app(app)

    # Init flask uploads
    configure_uploads(app, images)

    from app.views.views import app_pet as pet_blueprint
    app.register_blueprint(pet_blueprint)

    @app.errorhandler(403)
    def forbidden(error):
        title = 'Forbidden'
        return render_template('errors/403.html', title = title), 403

    @app.errorhandler(404)
    def page_not_found(error):
        title = 'Page not found'
        return render_template('errors/404.html',  title = title), 404

    @app.errorhandler(500)
    def internal_error_server(error):
        title = 'Inter error server'
        return render_template('errors/500.html',  title = title), 500

    return app
