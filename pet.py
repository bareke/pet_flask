from flask import Flask, flash, redirect, render_template
from flask import request, url_for, make_response, session
from flask_wtf.csrf import CSRFProtect

from forms.forms import PetForm, OwnerForm
from models.models import db, Pet
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())
#csrf = CSRFProtect(app)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    form_pet = PetForm(request.form)
    form_owner = OwnerForm(request.form)

    if request.method == 'POST' and form_pet.validate():
        session['owner'] = form_pet.owner.data
        pet = Pet(
                name = form_pet.name.data,
                race = form_pet.race.data,
                age = form_pet.age.data,
                owner = form_pet.owner.data,
                )
        db.session.add(pet)
        db.session.commit()
        flash('Thanks for register.')
        return redirect(url_for('registered_successful'))

    elif request.method == 'POST' and form_owner.validate():
        session['owner'] = form_owner.owner.data
        return redirect(url_for('query_pets'))

    return render_template('index.html', form_pet = form_pet, form_owner = form_owner)


@app.route('/query/')
def query_pets():
    pass
    if 'owner' in session:
        name = session['owner']
    query = Pet.query.filter(Pet.owner == name).all()
    return render_template('query.html', results = query)


@app.route('/registered')
def registered_successful():
    if 'owner' in session:
        name = session['owner']
    return render_template('registered.html', owner = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run()
