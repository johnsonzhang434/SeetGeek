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
testuser1 = User(email='test@test.com', name='testuser',
    password=generate_password_hash('test_frontendA1$')
)
testuser2 = User(
    email='tst123@testmail.org',
    name='testuser',
    password=generate_password_hash('test_frontendA1$')
)
testuser3 = User(
    email="this'isactuallyv{ok@wtf.lol",
    name='testuser',
    password=generate_password_hash('test_frontendA1$')
)

class R1TestPost(BaseCase):
    # Test form post 
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

    # test both password username empty
    def test_r1_post_2_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # try submit login without password or name 
        self.click("input[type='submit']")
        # should be email format  is incorrect 
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.")

    # test password empty
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_r1_post_2_2(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # enter user name  
        self.type("#email", "test_frontend@test.com")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.")

    # test no email 
    def test_r1_post_2_3(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # enter password but no name  
        self.type("#password", "test_frontendA1$")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.")

    # test invalid email formats
    def test_r1_post_3_1(self, *_):
        for i in ["Test.test.com", "test@test@test.com"]:
            # logout if logged in
            self.open(base_url + '/logout')
            # open login page
            self.open(base_url +'/login')
            # enter email  
            self.type("#email", i)
            # enter password but no name  
            self.type("#password", "test_frontendA1$")
            # try submit form 
            self.click("input[type='submit']")
            # should be email format is incorrect 
            self.assert_element("#message")
            self.assert_text("Email/password format is incorrect.")

    # test invalid email characters
    def test_r1_post_3_2(self, *_):
        for i in ["test\"(test,:;<>[\\]@test.com", "test\"test test@test.com", "tggg,,,@test.com"]:
            # logout if logged in
            self.open(base_url + '/logout')
            # open login page
            self.open(base_url +'/login')
            # enter email  
            self.type("#email", i)
            # enter password but no name  
            self.type("#password", "test_frontendA1$")
            # try submit form 
            self.click("input[type='submit']")
            # should be email format is incorrect 
            self.assert_element("#message")
            self.assert_text("Email/password format is incorrect.")

    # test valid emails

    @patch('qa327.backend.get_user', return_value=testuser1)
    def test_r1_post_3_3_1(self, *_):

        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # enter email  
        self.type("#email", 'test@test.com')
        # enter password but no name  
        self.type("#password", "test_frontendA1$")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.open(base_url)
        # validate that we are logged in (ie we can see the welcome header
        # and our name)
        self.assert_element("#welcome-header")
        self.assert_text("Hi testuser !")

    @patch('qa327.backend.get_user', return_value=testuser2)
    def test_r1_post_3_3_2(self, *_):

        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # enter email  
        self.type("#email", 'tst123@testmail.org')
        # enter password but no name  
        self.type("#password", "test_frontendA1$")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.open(base_url)
        # validate that we are logged in (ie we can see the welcome header
        # and our name)
        self.assert_element("#welcome-header")
        self.assert_text("Hi testuser !")

    @patch('qa327.backend.get_user', return_value=testuser3)
    def test_r1_post_3_3_3(self, *_):

        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url +'/login')
        # enter email  
        self.type("#email", "this'isactuallyv{ok@wtf.lol")
        # enter password but no name  
        self.type("#password", "test_frontendA1$")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.open(base_url)
        # validate that we are logged in (ie we can see the welcome header
        # and our name)
        self.assert_element("#welcome-header")
        self.assert_text("Hi testuser !")

