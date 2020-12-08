import pytest
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime 
# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test',
    password=generate_password_hash('Testing1!'),
    balance=5000
)

class R8Test(BaseCase):
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

        # Check if sell route is a valid request
        # validate that the current page shows a ticket-sell form
        # with test ticket's name, quantity, price, expr date
        self.assert_element("input[name='sell_name']")
        self.assert_element("input[name='sell_qty']")
        self.assert_element("input[name='sell_price']")
        self.assert_element("input[name='sell_date']")
        #Fill test ticket's name, quantity, price, expr date
        self.type("#sell_name","testticketone")
        self.type("#sell_qty", "20")
        self.type("#sell_price","10")
        self.type("#sell_date","20210901")
        # click Sell button
        self.click('input[value="Sell"]')
        # Check to see that the ticket has been posted and no error message appears
        self.assert_text("Ticket Posted for Sale")

        # refresh page
        self.open(base_url)
       
        # Check if buy route is a valid request
        # validate that the current page shows a ticket-buy form
        # with test ticket's name, quantity, price, expr date
        self.assert_element("input[name='buy_name']")
        self.assert_element("input[name='buy_qty']")
        self.type("#buy_name","testticketone")
        self.type("#buy_qty", "5")
        # click Buy button
        self.click('input[value="Buy"]')
        # Check to see that the ticket has been bought and no error message appears
        self.assert_text("Ticket Purchased")
        
        # refresh page
        self.open(base_url)

        # Check if update route is a valid request
        # validate that the current page shows a ticket-update form
        # with test ticket's name, quantity, price, expr date
        self.assert_element("input[name='orig_name']")
        self.assert_element("input[name='update_name']")
        self.assert_element("input[name='update_qty']")
        self.assert_element("input[name='update_price']")
        self.assert_element("input[name='update_date']")
        #Fill test ticket's name, quantity, price, expr date
        self.type("#orig_name","testticketone")
        self.type("#update_name","testticketthree")
        self.type("#update_qty", "25")
        self.type("#update_price","10")
        self.type("#update_date","20211001")
        # click update button
        self.click('input[value="Update"]')
        # Check to see that the updated ticket has been posted and no error message appears
        self.assert_text("Ticket Updated")
        # refresh page
        self.open(base_url)

        
        # Try and request an invalid request
        self.open(base_url + '/invalidrequest')
        # validate that you are redirected to 404 error page.
        self.assert_text("404 Error", "#message")



