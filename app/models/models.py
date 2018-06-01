from app.app import db

# Create yours models

class Person(db.Model):
    """Modelo Persona

    Person(id_person, name_person, last_name_person, telephone_person,
    email_person, name_profile_img)

    Relaciones:
        - Persona tendrá referencias de varias Mascotas

    Nota: lazy(perezosa) = True define como SQLAlchemy cargará los datos
    """
    id_person = db.Column(db.Integer, primary_key = True)
    name_person = db.Column(db.String(25), nullable = False)
    last_name_person = db.Column(db.String(25), nullable = False)
    telephone_person = db.Column(db.Integer(), nullable = False)
    email_person = db.Column(db.String(25), unique = True, nullable = False)

    name_profile_img = db.Column(db.String, default = 'default.jpg' , nullable = True)
    url_profile_img = db.Column(db.String, default = 'http://localhost:5000/static/profile_img/default.jpg' , nullable = True)

    # Relacion uno a muchos con la clase Mascota
    pets = db.relationship('Pet', backref = 'owner', lazy = True)

    def __repr__(self):
        return self.name_person


class Pet(db.Model):
    """Modelo Mascota

    Pet(id_pet, name_pet, type_pet, age_pet, name_profile_img)

    Nota: al registrar una mascota, el valor de adopcion siempre sera False

    Relaciones:
        - Mascota tendrá la llave primaria de Persona
    """
    id_pet = db.Column(db.Integer, primary_key = True)
    name_pet = db.Column(db.String(25), nullable = False)
    type_pet = db.Column(db.String(25), nullable = False)
    age_pet = db.Column(db.Integer(), nullable = False)
    adopt = db.Column(db.Boolean(), nullable = False, default = False)

    name_profile_img = db.Column(db.String, default = 'default.jpg' , nullable = True)
    url_profile_img = db.Column(db.String, default = 'http://localhost:5000/static/profile_img/default.jpg' , nullable = True)

    # Referencia a la clase Persona
    id_owner = db.Column(db.Integer,
                        db.ForeignKey('person.id_person'),
                        nullable = True)

    def __repr__(self):
        return self.name_pet
