from base64 import b64encode

from flask import Flask
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import make_response


from .forms.forms import PetForm, PersonForm, QueryPetForm
from .models.models import Pet, Person
from app.app import db

app_pet = Blueprint('app_pet', __name__)

@app_pet.route('/', methods = ['GET', 'POST'])
@app_pet.route('/index/', methods = ['GET', 'POST'])
def index():
    form_pet = PetForm(request.form)
    form_person = PersonForm(request.form)
    form_query_pet = QueryPetForm(request.form)
    if request.method == 'POST':
        flash('Thanks for register.')
        if form_person.validate():
            register_person(form_person)
            return redirect(url_for('app_pet.registered'))
        elif form_pet.validate():
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
    query = Pet.query.filter_by(type_pet = type_pet, adopt = False).all()
    return render_template('query.html', results = query)


@app_pet.route('/registered/')
def registered():
    return render_template('registered.html')


@app_pet.route('/details/<int:id_pet>')
def details_pet(id_pet):
    pet = Pet.query.filter_by(id_pet = id_pet).first()
    return render_template('details_pet.html', pet = pet)


@app_pet.route('/details')
def adopt():
    # TODO: Implementar la logica para adopción
    pass


def register_person(form_person):
    person = Person(
                    name_person = form_person.name_person.data,
                    last_name_person = form_person.last_name_person.data,
                    telephone_person = form_person.telephone_person.data,
                    email_person = form_person.email_person.data,
                    )
    db.session.add(person)
    db.session.commit()


def register_pet(form_pet):
    pet = Pet(
            name_pet = form_pet.name_pet.data,
            type_pet = form_pet.type_pet.data,
            age_pet = form_pet.age_pet.data,
            )
    db.session.add(pet)
    db.session.commit()
