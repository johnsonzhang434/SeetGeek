
import pytest
from seleniumbase import BaseCase
import qa327.backend as bn
from qa327_test.conftest import base_url
from unittest.mock import patch
from werkzeug.security import generate_password_hash, check_password_hash

class Tests1(BaseCase):
    def test_T1(self,*_):
        self.assertEqual(bn.validate_password(''), False)
    def test_T2(self,*_):
        self.assertEqual(bn.validate_password('AAAAAAAAA'), False)
    def test_T3(self,*_):
        self.assertEqual(bn.validate_password('AbCd12$'), True)
