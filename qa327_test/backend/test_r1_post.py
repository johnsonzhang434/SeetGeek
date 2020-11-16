import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from werkzeug.security import generate_password_hash, check_password_hash

test_user = User(
    email='test_frontend@test.com',
    name='testuser'
    password=generate_password_hash('test_frontendA1$')
)

class R1TestPost(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_r1_post_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # validate that there is an login element that says log in 
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_frontendA1$")
        self.click("input[type='submit']")
        self.open(base_url)
        self.assert_element("#welcome-header")
        self.assert_text("Hi testuser !")



