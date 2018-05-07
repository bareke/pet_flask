from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Create yours models

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25))
    type_pet = db.Column(db.String(25))
    age = db.Column(db.Integer())
    owner = db.Column(db.String(25))
    image_name = db.Column(db.String(100))
    data_image = db.Column(db.LargeBinary)
