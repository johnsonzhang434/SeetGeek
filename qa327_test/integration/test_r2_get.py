import pytest
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Test_frontend1!')
)

class R2Test(BaseCase):

    # If the user has logged in, redirect back to the user profile page /
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_r2_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend1!")
        # click enter button
        self.click('input[type="submit"]')
        # open register page
        self.open(base_url +'/register')
        # validate that current page (should be user profile page) contains welcome-header element
        self.assert_element("#welcome-header")

    # Otherwise, show the user registration page
    def test_r2_2(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/register')
        # validate that we are on the register page
        self.assert_element("input[value='Register']")

    # The registration page shows a registration form requesting: email, user name, password, password2
    def test_r2_3(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/register')
        #validate that the register page requests email, user name, password and password2 input
        self.assert_element("input[name='email']")
        self.assert_element("input[name='name']")
        self.assert_element("input[name='password']")
        self.assert_element("input[name='password2']")