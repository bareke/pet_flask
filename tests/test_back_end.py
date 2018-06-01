import os
import sys
import unittest

from flask_testing import TestCase

sys.path.append(os.getcwd())
from app.app import create_app, db, TestingConfig
from app.models.models import Pet, Person

# Tests Back-End

class TestBase(TestCase):
    """
    Config test base
    """
    def create_app(self):
        app = create_app()
        app.config.from_object(TestingConfig())
        return app

    def setUp(self):
        app = self.create_app()

        db.drop_all()
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestModels(TestBase):
    """
    Checkout server side application

    Test:
        - Create person model
        - Create pet model
        - Relationship of person and pet
    """
    def test_1_person_model(self):
        """
        Test create person
        """
        person = Person(
                        name_person = 'Cristian',
                        last_name_person = 'Ordonez',
                        telephone_person = '315',
                        email_person = 'cristian@pythonpopayan.com'
                        )
        db.session.add(person)
        db.session.commit()
        self.assertEqual(Person.query.count(), 1)

    def test_2_pet_model(self):
        """
        Test create pet
        """
        pet = Pet(
                name_pet = 'Salome',
                type_pet = 'Gato',
                age_pet = '3'
                )
        db.session.add(pet)
        db.session.commit()
        self.assertEqual(Pet.query.count(), 1)

    def test_3_person_adopt_pet(self):
        """
        Test person adopt pet
        """
        person = Person(
                        name_person = 'Cristian',
                        last_name_person = 'Ordonez',
                        telephone_person = '315',
                        email_person = 'cristian@pythonpopayan.com'
                        )

        pet = Pet(
                name_pet = 'Salome',
                type_pet = 'Gato',
                age_pet = '3'
                )
        pet.id_owner = person.id_person
        pet.adopt = True

        db.session.add(person)
        db.session.add(pet)
        db.session.commit()


class TestModelPerson(TestBase):
    """
    Check integrity of model Pet
    """
    pass


class TestModelPet(TestBase):
    """
    Check integrity of model Pet
    """
    def test_1_check_negative_age_pet(self):
        pet = Pet(
                name_pet = 'Salome',
                type_pet = 'Gato',
                age_pet = '-10'
                )
        db.session.add(pet)
        db.session.commit()

    def test_1_check_future_age_pet(self):
        pet = Pet(
                name_pet = 'Salome',
                type_pet = 'Gato',
                age_pet = '150'
                )
        db.session.add(pet)
        db.session.commit()


if __name__ == '__main__':
    unittest.main()
