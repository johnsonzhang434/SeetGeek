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

class R1Test(BaseCase):

    # If the user hasn't logged in, show the login page
    def test_r1_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # validate that there is a login element that says "Log In"
        self.assert_text('Log In', '#login')

    # The login page has a message that by default says 'Please login'
    def test_r1_2(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # validate that there is a message element that says "please login"
        self.assert_text('Please login', '#message')

    # If the user has logged in, redirect to the user profile page
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_r1_3(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend1!")
        # click enter button
        self.click('input[type="submit"]')
        # open login page again
        self.open(base_url +'/login')
        #validate that current page contains welcome-header element
        self.assert_element("#welcome-header")

    # The login page provides a login form which requests two fields: email and password
    def test_r1_4(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # validate that form requests email and password
        self.assert_element("form input[id='email']")
        self.assert_element("form input[id='password']")
