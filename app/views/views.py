from base64 import b64encode

from flask import Flask
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from app.forms.forms import PetForm
from app.forms.forms import PersonForm
from app.forms.forms import QueryPetForm
from app.forms.forms import AdoptPetForm
from app.models.models import Person
from app.models.models import Pet
from app.app import images
from app.app import db

app_pet = Blueprint('app_pet', __name__)

@app_pet.route('/', methods = ['GET', 'POST'])
@app_pet.route('/index/', methods = ['GET', 'POST'])
def index():
    form_pet = PetForm(request.form)
    form_person = PersonForm(request.form)
    form_query_pet = QueryPetForm(request.form)
    if request.method == 'POST':
        if form_person.validate():
            flash('Thanks for register.')
            if 'profile_img' in request.files:
                name_img = images.save(request.files['profile_img'])
                url_img = images.url(name_img)
                register_person(form_person, name_img, url_img)
            else:
                register_person(form_person)
            return redirect(url_for('app_pet.registered'))
        elif form_pet.validate():
            flash('Thanks for register.')
            if 'profile_img' in request.files:
                name_img = images.save(request.files['profile_img'])
                url_img = images.url(name_img)
                register_pet(form_pet, name_img, url_img)
            else:
                register_pet(form_pet)
            return redirect(url_for('app_pet.registered'))
        elif form_query_pet.validate():
            query_type_pet = form_query_pet.query_type_pet.data
            return redirect(url_for('app_pet.query_pets', type_pet = query_type_pet))
    forms = {
            'form_pet' : form_pet,
            'form_person' : form_person,
            'form_query_pet' : form_query_pet
            }
    return render_template('index.html', **forms)

@app_pet.route('/query/<type_pet>')
def query_pets(type_pet):
    query = Pet.query.filter_by(type_pet = type_pet).all()
    #query = Pet.query.filter_by(type_pet = type_pet, adopt = False).all()
    return render_template('query.html', results = query)

@app_pet.route('/registered/')
def registered():
    return render_template('registered.html')

@app_pet.route('/details/<int:id_pet>')
def details_pet(id_pet):
    form_adopt = AdoptPetForm()
    pet = Pet.query.filter_by(id_pet = id_pet).one()
    return render_template('details_pet.html', pet = pet, form_adopt = form_adopt)

@app_pet.route('/adopt/<int:id_pet>', methods = ['GET', 'POST'])
def adopt(id_pet):
    form_adopt = AdoptPetForm(request.form)
    if request.method == 'POST':
        if form_adopt.validate():
            pet = Pet.query.filter_by(id_pet = id_pet).one()
            email = form_adopt.email_person.data
            person = Person.query.filter_by(email_person = email).one()
            person_adopt_pet(pet, person)
            flash('Thanks for adopting a pet.')
            return render_template('details_pet.html', pet = pet, form_adopt = form_adopt)
    return render_template('adopt.html', form_adopt = form_adopt)

def person_adopt_pet(pet, person):
    pet.id_owner = person.id_person
    pet.adopt = True

    db.session.add(person)
    db.session.add(pet)
    db.session.commit()

def register_person(form_person, name_img = None, url_img = None):
    person = Person(
                    name_person = form_person.name_person.data,
                    last_name_person = form_person.last_name_person.data,
                    telephone_person = form_person.telephone_person.data,
                    email_person = form_person.email_person.data,
                    )
    if name_img and url_img:
        person.name_profile_img = name_img
        person.url_profile_img = url_img

    db.session.add(person)
    db.session.commit()

def register_pet(form_pet, name_img = None, url_img = None):
    pet = Pet(
            name_pet = form_pet.name_pet.data,
            type_pet = form_pet.type_pet.data,
            age_pet = form_pet.age_pet.data,
            )
    if name_img and url_img:
        pet.name_profile_img = name_img
        pet.url_profile_img = url_img

    else:
        type_img_default = {
            'Perro': ['dog_default.png', 'http://localhost:5000/static/profile_img/dog_default.png'],
            'Gato': ['cat_default.png', 'http://localhost:5000/static/profile_img/cat_default.png'],
        }
        if pet.type_pet in type_img_default:
            list = type_img_default[pet.type_pet]
            pet.name_profile_img = list[0]
            pet.url_profile_img = list[1]

    db.session.add(pet)
    db.session.commit()
