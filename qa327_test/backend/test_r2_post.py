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

testuser4 = User(email='test@test.com', name='testuser',
    password=generate_password_hash("aaaaa1$A")
)
testuser5 = User(email='test@test.com', name='testuser',
    password=generate_password_hash('abct)432A')
)
class R2TestPost(BaseCase):
    # Test form post 
    def test_r2_post_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter user name and password
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testuser")
        self.type("#password", "test_frontendA1$")
        self.type("#password2", "test_frontendA1$")
        # try submit form 
        self.click("input[type='submit']")
        self.assert_text("Please Login")

    # test both password username empty
    def test_r2_post_2_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # try submit register without password or name 
        self.click("input[type='submit']")
        # should be email format  is incorrect 
        self.assert_element("#message")
        self.assert_text("email format is incorrect")

    # test password empty
    def test_r2_post_2_2(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter user name  
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testuser")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_element("#message")
        self.assert_text("password format is incorrect")

    # test no email 
    def test_r2_post_2_3(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter password but no name  
        self.type("#password", "test_frontendA1$")
        self.type("#name", "testuser")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_element("#message")
        self.assert_text("email format is incorrect")

    # test invalid email formats
    def test_r2_post_2_5(self, *_):
        for i in ["Test.test.com", "test@test@test.com"]:
            # logout if logged in
            self.open(base_url + '/logout')
            # open register page
            self.open(base_url +'/register')
            # enter email  
            self.type("#email", i)
            # enter password but no name  
            self.type("#name", "testuser")
            self.type("#password", "test_frontendA1$")
            # try submit form 
            self.click("input[type='submit']")
            # should be email format is incorrect 
            self.assert_element("#message")
            self.assert_text("email format is incorrect")

    # test invalid email characters
    def test_r2_post_2_6(self, *_):
        for i in ["test\"(test,:;<>[\\]@test.com", "test\"test test@test.com", "tggg,,,@test.com"]:
            # logout if logged in
            self.open(base_url + '/logout')
            # open register page
            self.open(base_url +'/register')
            # enter email  
            self.type("#email", i)
            self.type("#name", "testuser")
            # enter password but no name  
            self.type("#password", "test_frontendA1$")
            # try submit form 
            self.click("input[type='submit']")
            # should be email format is incorrect 
            self.assert_element("#message")
            self.assert_text("email format is incorrect")

    # test valid emails
    def test_r2_post_2_7_1(self, *_):

        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", 'test@test.com')
        self.type("#name", "testuser")
        # enter password but no name  
        self.type("#password", "test_frontendA1$")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.open(base_url)
        # validate that we are logged in (ie we can see the welcome header
        # and our name)
        self.assert_text("Please login")

    def test_r2_post_2_7_2(self, *_):

        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", 'tst123@testmail.org')
        self.type("#name", "testuser")
        # enter password but no name  
        self.type("#password", "test_frontendA1$")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.open(base_url)
        # validate that we are logged in (ie we can see the welcome header
        # and our name)
        self.assert_text("Please login")

    def test_r2_post_2_7_3(self, *_):

        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "this'isactuallyv{ok@wtf.lol")
        self.type("#name", "testuser")
        # enter password but no name  
        self.type("#password", "test_frontendA1$")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.open(base_url)
        # validate that we are logged in (ie we can see the welcome header
        # and our name)
        self.assert_text("Please login")

    def test_r2_post_2_8(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "12345678901234567890123456789012345678901234567890123456789012341234567890123456789012345678901234567890123456789012345678901234@test.com" )
        self.type("#name", "testuser")
        # enter password but no name  
        self.type("#password", "test_frontendA1$")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_element("#message")
        self.assert_text("email format is incorrect")

    # test invalid email format 
    def test_r2_post_2_9(self, *_):
        for i in ["test..test@test.com", "test.test@test..com",".test@test.com", "test.@test.com"]:
            # logout if logged in
            self.open(base_url + '/logout')
            # open register page
            self.open(base_url +'/register')
            # enter email  
            self.type("#email", i)
            self.type("#name", "testuser")
            # enter password but no name  
            self.type("#password", "test_frontendA1$")
            # try submit form 
            self.click("input[type='submit']")
            # should be email format is incorrect 
            self.assert_text("email format is incorrect")

    # password too short 
    def test_r2_post_2_10(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test@test.com")
        # enter password but no name  
        self.type("#name", "testuser")
        self.type("#password", "a1A!")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_text("password format is incorrect")

    # password missing special character
    def test_r2_post_2_11(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test@test.com")
        self.type("#name", "testuser")
        # enter password but no name  
        self.type("#password", "aaaAAA111")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_element("#message")
        self.assert_text("password format is incorrect")



    # password missing lowercase 
    def test_r2_post_2_12(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test@test.com")
        self.type("#name", "testuser")
        # enter password but no name  
        self.type("#password", "AAAA1111!!!!")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_text("password format is incorrect")


    # password missing uppercase  
    def test_r2_post_2_14(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test@test.com")
        self.type("#name", "testuser")
        # enter password but no name  
        self.type("#password", "aaa111!!!!")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_text("password format is incorrect")


    # test that valid passwords work
    def test_r2_post_2_15_1(self, *_):

        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", 'test@test.com')
        self.type("#name", "testuser")
        # enter password but no name  
        self.type("#password", "aaaaa1$A")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.open(base_url)
        # validate that we are logged in (ie we can see the welcome header
        # and our name)
        self.assert_text("Please login")

    # test that valid passwords work
    def test_r2_post_2_15_2(self, *_):

        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test@test.com")
        self.type("#name", "testuser")
        # enter password but no name  
        self.type("#password", "abct)432A")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.open(base_url)
        # validate that we are logged in (ie we can see the welcome header
        # and our name)
        self.assert_text("Please login")


    def test_r2_post_3_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test@test.com")
        self.type("#name", "testuser")
        # enter password but no name  
        self.type("#password", "abct)432A")
        self.type("#password2", "notTheS4m3!")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_text("passwords do not match")

    def test_r2_post_3_2(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter user name and password
        self.type("#email", "test_frontend1@test.com")
        self.type("#name", "testuser")
        self.type("#password", "test_frontendA1$")
        self.type("#password2", "test_frontendA1$")
        # try submit form 
        self.click("input[type='submit']")
        self.assert_text("Please Login")


    def test_r2_post_4_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test@test.com")
        self.type("#name", "$+-=")
        # enter password but no name  
        self.type("#password", "abct)432A")
        self.type("#password2", "abct)432A")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_text("name format is incorrect")

    def test_r2_post_4_2(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test@test.com")
        # enter password but no name  
        self.type("#password", "abct)432A")
        self.type("#password2", "abct)432A")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_text("name format is incorrect")

    def test_r2_post_4_3(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test@test.com")
        self.type("#name", " test")
        # enter password but no name  
        self.type("#password", "abct)432A")
        self.type("#password2", "abct)432A")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_text("name format is incorrect")

    def test_r2_post_4_4(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test@test.com")
        self.type("#name", "test ")
        # enter password but no name  
        self.type("#password", "abct)432A")
        self.type("#password2", "abct)432A")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_text("name format is incorrect")

    def test_r2_post_4_5(self, *_):
        for i, n in enumerate(['bob', 'test123', 'bob ashtast']):
            # logout if logged in
            self.open(base_url + '/logout')
            # open register page
            self.open(base_url +'/register')
            # enter email  
            self.type("#email", "test"+str(i)+"@test.com")
            self.type("#name", n)
            # enter password but no name  
            self.type("#password", "abct)432A")
            self.type("#password2", "abct)432A")
            # try submit form 
            self.click("input[type='submit']")
            # should be email format is incorrect 
            self.assert_text("Please Login")

    def test_r2_post_5_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test@test.com")
        self.type("#name", "uu")
        # enter password but no name  
        self.type("#password", "abct)432A")
        self.type("#password2", "abct)432A")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_text("name format is incorrect")
    # test that redirected to / with valid email pw

    def test_r2_post_5_2(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test@test.com")
        self.type("#name", "12345678901234567890")
        # enter password but no name  
        self.type("#password", "abct)432A")
        self.type("#password2", "abct)432A")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_text("name format is incorrect")

    def test_r2_post_5_3(self, *_):
        for i, n in enumerate(['888', '2345678901234567890']):
            # logout if logged in
            self.open(base_url + '/logout')
            # open register page
            self.open(base_url +'/register')
            # enter email  
            self.type("#email", "test"+str(i+5)+"@test.com")
            self.type("#name", n)
            # enter password but no name  
            self.type("#password", "abct)432A")
            self.type("#password2", "abct)432A")
            # try submit form 
            self.click("input[type='submit']")
            # should be email format is incorrect 
            self.assert_text("Please Login")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_r2_post_7_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testuser")
        self.type("#password", "Password1$")
        self.type("#password2", "Password1$")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_element("#message")
        self.assert_text("this email has been ALREADY used")

    # incorrect email
    def test_r2_post_7_2(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "new@email.com")
        self.type("#name", "testuser")
        self.type("#password", "Password1$")
        self.type("#password2", "Password1$")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_element("#message")
        self.assert_text("Please Login")

    # incorrect email and password
    def test_r2_post_8(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url +'/register')
        # enter email  
        self.type("#email", "new1@email.com")
        self.type("#name", "testuser")
        self.type("#password", "Password1$")
        self.type("#password2", "Password1$")
        # try submit form 
        self.click("input[type='submit']")
        # should be email format is incorrect 
        self.assert_element("#message")
        self.assert_text("Please Login")
        self.type("#email", "new1@email.com")
        self.type("#password", "Password1$")
        self.click("input[type='submit']")
        self.assert_text("Your Current Balance is 5000")
