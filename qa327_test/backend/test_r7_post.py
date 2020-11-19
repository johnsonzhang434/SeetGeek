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
class R7TestPost(BaseCase):
    # Logout will invalidate the current session and redirect to 
    # the login page. After logout the user should not be able to
    # access restricted pages
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_r1_post_1(self, *_):
        # logout 
        self.open(base_url + '/logout')
        # check if we are on the login page now
        self.assert_text("Please Login")
        # try to go to /
        self.open(base_url)
        # validate that we are still on the login page
        self.assert_text("Please Login")

