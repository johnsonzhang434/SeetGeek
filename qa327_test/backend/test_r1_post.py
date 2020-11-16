import pytest
from seleniumbase import BaseCase
from qa327.models import db, User
from qa327_test.conftest import base_url
from unittest.mock import patch
from werkzeug.security import generate_password_hash, check_password_hash

test_user = User(
    email='test_frontend@test.com',
    name='testuser',
    password=generate_password_hash('test_frontendA1$')
)

class R1TestPost(BaseCase):
    # Test R1.P.1
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_r1_post_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # enter user name and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_frontendA1$")
        # try submit form 
        self.click("input[type='submit']")
        self.open(base_url)
        # validate that we are logged in (ie we can see the welcome header
        # and our name)
        self.assert_element("#welcome-header")
        self.assert_text("Hi testuser !")

    def test_r1_post_2_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # try submit login without password or name 
        self.click("input[type='submit']")
        # should be email formaet is incorrect 
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.")




