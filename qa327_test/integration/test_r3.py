import pytest
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime 

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test',
    password=generate_password_hash('Testing1!'),
    balance=5000
)

# Mock a sample ticket with sample date
test_ticket = Ticket(
    name="test_ticket_yo",
    owner="test_frontend@test.com", 
    qty=10, 
    price=10, 
    exp=datetime(2021,9,1)
)


class R3Test(BaseCase):
    
    # If the user is not logged in, redirect to login page
    def test_r3_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # validate that there is a login element that says "Log In"
        self.assert_text("Log In", "#login")

    @patch('qa327.backend.get_user', return_value=test_user)
    # This page shows a header 'Hi {}'.format(user.name)
    def test_r3_2(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Testing1!")
        # click enter button
        self.click('input[type="submit"]')
        
        # valdidate that there is a header 'Hi {}'.format(user.name) element
        self.assert_text("Hi test !", "#welcome-header")

    @patch('qa327.backend.get_user', return_value=test_user)
    # This page shows user balance. 
    def test_r3_3(self,*_):
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
        # validate that the current page shows a user balance
        self.assert_text("Your Current Balance is 5000", "#balance")

    @patch('qa327.backend.get_user', return_value=test_user)
    # This page shows a logout link, pointing to /logout
    def test_r3_4(self,*__):
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
        # validate that the current page shows a logout link
        self.is_link_text_present("logout")
        # validate that when the logout link is clicked, you are redirected to /logout
        self.click_link_text("logout")
   
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    # This page lists all available tickets. Information including the quantity of each ticket, 
    # the owner's email, and the price, for tickets that are not expired.
    def test_r3_5(self,*_):
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
        # validate that all available tickets are not expired.
        self.assert_text("Here are all available tickets")
        # validate that valid tickets have a #name, #quantity, #owner's email, and #price element.
        self.assert_text("test_ticket_yo", "#display_name")
        self.assert_text("test_frontend@test.com", "#display_owner")
        self.assert_text(10, "#display_qty")
        self.assert_text("2021-09-01 00:00:00",  "#display_exp")
        self.assert_text(10, "#display_price")
        #Check if tickets are expired
        today = datetime.now()
        exp = (self.get_element("#display_exp").text).split()
        exp_date = datetime.strptime(exp[0], '%Y-%m-%d')
        self.assert_true(exp_date>today)
    
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    # This page contains a form that a user can submit new tickets for sell. 
    # Fields: name, quantity, price, expiration date
    def test_r3_6(self,*_):
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
        self.type("#sell_name","test_ticket_yo")
        self.type("#sell_qty", "10")
        self.type("#sell_price","10")
        self.type("#sell_date","20210901")
        # click Sell button
        self.click('input[value="Sell"]')
        #Refresh the page
        self.refresh_page()

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    # This page contains a form that a user can buy new tickets. Fields: name, quantity
    def test_r3_7(self,*_):
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
        # validate that the current page shows a ticket-buy form
        # with test ticket's name, quantity, price, expr date
        self.assert_element("input[name='buy_name']")
        self.assert_element("input[name='buy_qty']")

        #Fill test ticket's name, quantity
        self.type("#buy_name","test_ticket_yo")
        self.type("#buy_qty", "10")
        
        # click Buy button
        self.click('input[value="Buy"]')
        #Refresh the page
        self.refresh_page()
    
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    # The ticket-selling form can be posted to /sell
    def test_r3_8(self,*_):
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
        self.type("#sell_name","test_ticket_yo")
        self.type("#sell_qty", "10")
        self.type("#sell_price","10")
        self.type("#sell_date","20210901")
        # click Sell button
        self.click('input[value="Sell"]')
        #Refresh the page
        self.refresh_page()

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    #The ticket-buying form can be posted to /buy
    def test_r3_9(self,*_):
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
        # validate that the current page shows a ticket-buy form
        # with test ticket's name, quantity, price, expr date
        self.assert_element("input[name='buy_name']")
        self.assert_element("input[name='buy_qty']")

        #Fill test ticket's name, quantity
        self.type("#buy_name","test_ticket_yo")
        self.type("#buy_qty", "10")
        
        # click Buy button
        self.click('input[value="Buy"]')
        #Refresh the page
        self.refresh_page()

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    # The ticket-update form can be posted to /update
    def test_r3_10(self,*_):
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
        # validate that the current page shows a ticket-update form
        # with test ticket's name, quantity, price, expr date
        self.assert_element("input[name='update_name']")
        self.assert_element("input[name='update_qty']")
        self.assert_element("input[name='update_price']")
        self.assert_element("input[name='update_date']")
        # click Update button
        self.click('input[value="Update"]')
        #Refresh the page
        self.refresh_page()
    