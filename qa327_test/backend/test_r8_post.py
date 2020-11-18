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
    # Test form post 
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_r1_post_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        self.assert_text("Please login")
        self.open(base_url)
        # validate that we are logged in (ie we can see the welcome header
        # and our name)
        self.assert_text("Please login")

