import pytest
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from qa327_test.conftest import base_url
from unittest.mock import patch
from werkzeug.security import generate_password_hash, check_password_hash

class R1Test(BaseCase):
    pass
    
    # For any other requests except the ones above, the system should return a 404 error
    def test_r8_1(self, *_):
        # Try and request an invalid request
        self.open(base_url + '/invalidrequest')
        # validate that you are redirected to 404 error page.
        self.assert_text("404 Error", "#message")
    





