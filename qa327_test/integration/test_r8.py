import pytest
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test',
    password=generate_password_hash('Testing1!'),
    balance=5000
)

class R1Test(BaseCase):
    pass
    
    # For any other requests except the ones above, the system should return a 404 error
    def test_r8_1(self, *_):
        # Try and request an invalid request
        self.open(base_url + '/invalidrequest')
        # validate that you are redirected to 404 error page.
        self.assert_text("404 Error", "#message")
    
    # For valid requests, the system should not return 404 error.
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_r8_2(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # validate that there is a login element that says "Log In"
        self.assert_text("Log In", "#login")
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Testing1!")
        # click enter button
        self.click('input[type="submit"]')
        # Open Home Page
        self.open(base_url)
        # valdidate that there is a header 'Hi {}'.format(user.name) element
        self.assert_text("Hi test !", "#welcome-header")
        # Try and request an invalid request
        self.open(base_url + '/invalidrequest')
        # validate that you are redirected to 404 error page.
        self.assert_text("404 Error", "#message")
    
        # Requests below are not ready yet, system will lead to 404 error if requested
        # self.open(base_url +'/buy')
        # self.open(base_url + '/sell')
        # self.open(base_url + '/update')




