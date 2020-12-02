import pytest
from seleniumbase import BaseCase
from qa327.models import db, User, Ticket
from qa327_test.conftest import base_url
from unittest.mock import patch
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test',
    password=generate_password_hash('Testing1!'),
    balance=5000
)

class R4Test(BaseCase):
    
    @patch('qa327.backend.get_user', return_value=test_user)
    #Check if the selling actions fail when the ticket quantity is 0 or less.
    def test_r4_3_2(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Testing1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        self.assert_text("Hi test !", "#welcome-header")
        # validate that the current page shows a ticket-sell form
        # with test ticket's name, quantity, price, expr date
        self.assert_element("input[name='sell_name']")
        self.assert_element("input[name='sell_qty']")
        self.assert_element("input[name='sell_price']")
        self.assert_element("input[name='sell_date']")

        #Fill test ticket's name, quantity, price, expr date
        self.type("#sell_name","testticket")
        # quantity <= 0
        self.type("#sell_qty", "0")
        self.type("#sell_price","10")
        self.type("#sell_date","20210901")
        # click Sell button
        self.click('input[value="Sell"]')

        #Check to see that the ticket has not been posted and error message appears
        self.assert_text("Ticket quantity must be greater than (0)")
        
    
    @patch('qa327.backend.get_user', return_value=test_user)
    # Check if the selling actions fail when the ticket quantity is greater than 100
    def test_r4_3_3(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Testing1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        self.assert_text("Hi test !", "#welcome-header")
        # validate that the current page shows a ticket-sell form
        # with test ticket's name, quantity, price, expr date
        self.assert_element("input[name='sell_name']")
        self.assert_element("input[name='sell_qty']")
        self.assert_element("input[name='sell_price']")
        self.assert_element("input[name='sell_date']")

        #Fill test ticket's name, quantity, price, expr date
        self.type("#sell_name","testticket")
        # quantity > 100
        self.type("#sell_qty", "101")
        self.type("#sell_price","10")
        self.type("#sell_date","20210901")
        # click Sell button
        self.click('input[value="Sell"]')
    
        #Check to see that the ticket has not been posted and error message appears
        self.assert_text("Maxiumum ticket quantity is (100)")
    
    @patch('qa327.backend.get_user', return_value=test_user)
    # Check if the selling actions succeed when the ticket price is between 10 and 100
    def test_r4_4_1(self,*_):
         # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Testing1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        self.assert_text("Hi test !", "#welcome-header")
        # validate that the current page shows a ticket-sell form
        # with test ticket's name, quantity, price, expr date
        self.assert_element("input[name='sell_name']")
        self.assert_element("input[name='sell_qty']")
        self.assert_element("input[name='sell_price']")
        self.assert_element("input[name='sell_date']")
        
        #Fill test ticket's name, quantity, price, expr date
        self.type("#sell_name","testticketone")
        self.type("#sell_qty", "10")
        self.type("#sell_price","10")
        self.type("#sell_date","20210901")
        # click Sell button
        self.click('input[value="Sell"]')

        # Check to see that the ticket has been posted and no error message appears
        self.assert_text("Ticket Posted for Sale")
        # refresh the page
        self.open(base_url)
        # Check to see that the ticket has been posted and no error message appears
        self.assert_text("testticketone")
    
    @patch('qa327.backend.get_user', return_value=test_user)
    # Check if the selling actions fail when the ticket price is less than 10
    def test_r4_4_2(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Testing1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        self.assert_text("Hi test !", "#welcome-header")
        # validate that the current page shows a ticket-sell form
        # with test ticket's name, quantity, price, expr date
        self.assert_element("input[name='sell_name']")
        self.assert_element("input[name='sell_qty']")
        self.assert_element("input[name='sell_price']")
        self.assert_element("input[name='sell_date']")

        #Fill test ticket's name, quantity, price, expr date
        self.type("#sell_name","testticket")
        self.type("#sell_qty", "10")
        # price < 10
        self.type("#sell_price","9")
        self.type("#sell_date","20210901")
        # click Sell button
        self.click('input[value="Sell"]')
        
        #Check to see that the ticket has not been posted and an error message appears
        self.assert_text("Ticket price must be at least $10")

    @patch('qa327.backend.get_user', return_value=test_user)
    # Check if the selling actions fail when the ticket price is greater than 100
    def test_r4_4_3(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Testing1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        self.assert_text("Hi test !", "#welcome-header")
        # validate that the current page shows a ticket-sell form
        # with test ticket's name, quantity, price, expr date
        self.assert_element("input[name='sell_name']")
        self.assert_element("input[name='sell_qty']")
        self.assert_element("input[name='sell_price']")
        self.assert_element("input[name='sell_date']")

        #Fill test ticket's name, quantity, price, expr date
        self.type("#sell_name","testticket")
        self.type("#sell_qty", "10")
        # price > 100
        self.type("#sell_price","101")
        self.type("#sell_date","20210901")
        # click Sell button
        self.click('input[value="Sell"]')
        
        #Check to see that the ticket has not been posted and an error message appears
        self.assert_text("Maximum ticket price is $100")
    
    @patch('qa327.backend.get_user', return_value=test_user)
    # Check if the selling actions succeed when the ticket date is in the correct format
    def test_r4_5_1(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Testing1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        self.assert_text("Hi test !", "#welcome-header")
        # validate that the current page shows a ticket-sell form
        # with test ticket's name, quantity, price, expr date
        self.assert_element("input[name='sell_name']")
        self.assert_element("input[name='sell_qty']")
        self.assert_element("input[name='sell_price']")
        self.assert_element("input[name='sell_date']")

        #Fill test ticket's name, quantity, price, expr date
        self.type("#sell_name","testtickettwo")
        self.type("#sell_qty", "20")
        self.type("#sell_price","10")
        self.type("#sell_date","20210901")
        # click Sell button
        self.click('input[value="Sell"]')
        
        # Check to see that the ticket has been posted and no error message appears
        self.assert_text("Ticket Posted for Sale")
        # refresh the page
        self.open(base_url)
        # Check to see that the ticket has been posted and no error message appears
        self.assert_text("testtickettwo")
    