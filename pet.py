from base64 import b64encode

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import make_response
from flask_wtf.csrf import CSRFProtect

from forms.forms import PetForm, OwnerForm
from models.models import db, Pet
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())
csrf = CSRFProtect(app)


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index/', methods = ['GET', 'POST'])
def index():
    if  request.method == 'POST':
        form_pet = PetForm(request.form)
        form_owner = OwnerForm(request.form)

        if form_pet.validate():
            file = request.files['file']
            pet = Pet(
                    name = form_pet.name.data,
                    type_pet = form_pet.type_pet.data,
                    age = form_pet.age.data,
                    owner = form_pet.owner.data,
                    image_name = file.filename,
                    data_image = file.read()
                    )
            db.session.add(pet)
            db.session.commit()
            flash('Thanks for register.')
            response = make_response(redirect('registered'))
            response.set_cookie('owner', form_owner.owner.data)
            return response

        elif form_owner.validate():
            owner = form_owner.owner.data
            return redirect(url_for('query_pets', owner = owner))
    else:
        form_pet = PetForm()
        form_owner = OwnerForm()
        return render_template('index.html', form_pet = form_pet, form_owner = form_owner)


@app.route('/query/<owner>')
def query_pets(owner):
    query = Pet.query.filter(Pet.owner == owner).first()
    image = b64encode(query.data_image).decode('ascii')
    return render_template('query.html', result = query, image = image)


@app.route('/registered/')
def registered():
    owner = request.cookies.get('owner')
    return render_template('registered.html', owner = owner)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run()
