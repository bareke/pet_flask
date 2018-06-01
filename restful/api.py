from flask import Flask
from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Api
from flask_restful import Resource

from app.app import create_app, db
from app.models.models import Pet

def create_api():
    app = create_app()
    api = Api(app)

    # Resources routing
    api.add_resource(PetList, '/pets')
    api.add_resource(PetApi, '/pets/<id_pet>')

    return app

def abort_if_todo_doesnt_exist(id_pet):
    pet = Pet.query.filter(Pet.id_pet == id_pet).first()
    if not pet:
        abort(404, message="Pet {} doesn't exist".format(id_pet))
    return pet


# Arg query for POST
parser = reqparse.RequestParser()
parser.add_argument('id_pet')


class PetApi(Resource):
    """
    Shows a single pet and lets you delete a pet

    Examples usage:
        - GET a single pet
        curl http://localhost:5000/pets/1

        - DELETE a pet
        curl http://localhost:5000/pets/2 -X DELETE

        - PUT a pet
        curl http://localhost:5000/pets/1 -d "id_pet=1" -X PUT
    """
    def get(self, id_pet):
        pet = abort_if_todo_doesnt_exist(id_pet)
        return pet.name_pet

    def delete(self, id_pet):
        pet = abort_if_todo_doesnt_exist(id_pet)
        if pet:
            db.session.delete(pet)
            db.session.commit()
        return '', 204

    def put(self, id_pet):
        args = parser.parse_args()
        pet = Pet.query.filter_by(id_pet = id_pet).first()
        if pet:
            pet.name_pet = 'Changed name pet'
            db.session.commit()
        else:
            pet = {'name_pet': 'PetApi', 'type_pet': 'PUT', 'age_pet': '5'}
            register = Pet(name_pet = pet['name_pet'],
                        type_pet = pet['type_pet'],
                        age_pet = pet['age_pet']
                        )
            db.session.add(register)
            db.session.commit()
        return id_pet, 201


class PetList(Resource):
    """
    Shows a list of all pets, and lets you POST to add new pets

    Example usage:
        - GET the list
        curl http://localhost:5000/pets

        - Add a new pet
        curl http://localhost:5000/pets -d "id_pet=99" -X POST
    """
    def get(self):
        pets = Pet.query.all()
        list_pets = []
        for pet in pets:
            list_pets.append({
                            'id_pet' : pet.id_pet,
                            'name_pet' : pet.name_pet,
                            'type_pet' : pet.type_pet,
                            'age_pet' : pet.age_pet
                            })
        return list_pets

    def post(self):
        args = parser.parse_args()
        if 'id_pet' is not args and args.get('id_pet'):
            id_pet = args['id_pet']
            pet = {'name_pet': 'PetList', 'type_pet': 'POST', 'age_pet': '8'}
            db_pet = Pet(name_pet = pet['name_pet'],
                        type_pet = pet['type_pet'],
                        age_pet = pet['age_pet']
                        )
            db.session.add(db_pet)
            db.session.commit()
            return id_pet, 201
        return '', 204
