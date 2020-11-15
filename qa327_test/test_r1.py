import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

class R1Test(BaseCase):

    def test_r1_1(self, *_):
        # logout if logged in
        self.open(base_url, '/logout')
        # open login page
        self.open(base_url, '/login')
        # validate that there is an login element that says log in 
        self.assert_text('Log In', '#login')





