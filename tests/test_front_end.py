import os
import unittest
from time import sleep

from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from app.app import create_app, db, TestingConfig

# Tests Front-End

class FrontTestCase(LiveServerTestCase):
    """
    Checkout client side application

    Test:
        - Register pet
        - Query pets
    """
    def create_app(self):
        app = create_app()
        app.config.from_object(TestingConfig())
        return app

    def setUp(self):
        # Init Selenium
        exe = os.getcwd() + '/geckodriver'
        self.selenium = webdriver.Firefox(executable_path = exe)
        super(FrontTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(FrontTestCase, self).tearDown()

    def test_1_register_pet(self):
        self.selenium.get('http://127.0.0.1:5000/')
        sleep(3)

        #Centra la vista en el formulario de registro
        self.selenium.find_element_by_link_text('Register pet').click()
        sleep(2)

        # Busca los campos del formulario donde ingresara los datos
        name_pet = self.selenium.find_element_by_id('name_pet')
        type_pet = self.selenium.find_element_by_id('type_pet')
        age_pet = self.selenium.find_element_by_id('age_pet')

        submit = self.selenium.find_element_by_name('register pet')
        # Ingresa los datos
        sleep(1)

        name_pet.send_keys('Selenium')
        sleep(0.5)
        type_pet.send_keys('Software')
        sleep(0.5)
        age_pet.send_keys('14')
        sleep(0.5)

        # Register a pet
        submit.click()
        sleep(3)

    def test_2_query_pets(self):
        self.selenium.get('http://127.0.0.1:5000/')
        sleep(3)

        #Centra la vista en el formulario de busqueda
        self.selenium.find_element_by_link_text('Adopt pet').click()
        sleep(2)

        submit = self.selenium.find_element_by_name('query pet')
        sleep(2)
        owner = self.selenium.find_element_by_id('query_type_pet')
        sleep(0.5)

        owner.send_keys('Software')
        sleep(1)

        submit.click()
        sleep(3)

if __name__ == '__main__':
    unittest.main()
