import pytest
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Test_frontend1!')
)

# Mock a sample ticket
test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=10,
    price=10,
    date='20210901'
)

class R3Test(BaseCase):
    
    # If the user is not logged in, redirect to login page
    def test_r3_1(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # validate that there is a login element that says "Log In"
        self.assert_text('Log In', '#login')

    
    # This page shows a header 'Hi {}'.format(user.name)
    def test_r3_2(self, *_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend1!")
        # click enter button
        self.click('input[type="submit"]')
        
        # open home page
        self.open(base_url)
        # valdidate that there is a header 'Hi {}'.format(user.name) element
        self.assert_text("Hi test_frontend", "#welcome-header h2")

    # This page shows user balance. 
    def test_r3_3(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        # open home page
        self.open(base_url)
        # validate that the current page shows a user balance
        self.assert_text("Your Current Balance is ", "#balance h3")

    # This page shows a logout link, pointing to /logout
    def test_r3_4(self,*__):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        # open home page
        self.open(base_url)
        # validate that the current page shows a logout link
        self.assert_text("logout", "#logout")
        # validate that when the logout link is clicked, you are redirected to /logout
        self.open(base_url + '/logout')
    
    #This page lists all available tickets. Information including the quantity of each ticket, 
    # the owner's email, and the price, for tickets that are not expired.
    def test_r3_5(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        # open home page
        self.open(base_url)
        # validate that all available tickets are not expired.
        self.assert_element("#tickets div h4")
        self.assert_text("date", "#date")
        # validate that valid tickets have a #quantity, #owner's email, and #price element.
        self.assert_text("quantity", "#quantity")
        self.assert_text("owners email", "#email")
        self.assert_text("price", "#price")
        
    #This page contains a form that a user can submit new tickets for sell. 
    # Fields: name, quantity, price, expiration date
    def test_r3_6(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        # open home page
        self.open(base_url)
        #validate that the current page shows a ticket-sell form
        #Fill test ticket's name, quantity, price, expr date
        self.assert_text("Sell Ticket", "#sell")
        self.assert_text("Ticket Name:", "#sell_name")
        self.assert_text("Quantity:", "#sell_qty")
        self.assert_text("Ticket Price:", "#sell_price")
        self.assert_text("Expiration Date:","#sell_date")
       

    # This page contains a form that a user can buy new tickets. Fields: name, quantity
    def test_r3_7(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        # open home page
        self.open(base_url)
        #validate that the current page shows a ticket-buy form
        #Fill test ticket's name, quantity, price, expr date
        self.assert_text("Buy Ticket", "#buy")
        self.assert_text("Ticket Name:","#buy_name")
        self.assert_text("Quantity:","#buy_qty")

    # The ticket-selling form can be posted to /sell
    def test_r3_8(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        # open home page
        self.open(base_url)
        #validate that the current page shows a ticket-sell form
        #Fill test ticket's name, quantity, price, expr date
        self.assert_text("Sell Ticket", "#sell")
        self.type("#sell_name","test_ticket_yo")
        self.type("#sell_qty", "10")
        self.type("#sell_price","10")
        self.type("#sell_date","20210901")
        # click enter button
        self.click('input[type="submit"]')
        # Refresh page
        # validate that the ticket has been uploaded for sale on user profile page
        self.open(base_url)

    #The ticket-buying form can be posted to /buy
    def test_r3_9(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        # open home page
        self.open(base_url)
        # validate that the current page shows a ticket-buy form
        # Fill test ticket's name, quantity, price, expr date
        self.assert_text("Buy Ticket", "#buy")
        self.type("#buy_name","test_ticket_yo")
        self.type("#buy_qty","10")

        # click enter button
        self.click('input[type="submit"]')
        # Refresh page
        # validate that the ticket has been bought on user profile page
        self.open(base_url)

    # The ticket-update form can be posted to /update
    def test_r3_10(self,*_):
        # logout if logged in
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill test user's email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend1!")
        # click enter button
        self.click('input[type="submit"]')
        # validate that there is no error and that we are redirected to /
        # open home page
        self.open(base_url)
        # validate that the current page shows a ticket-update form
        # Fill test ticket's name, quantity, price, expr date
        self.assert_text("Update Ticket", "#update")
        self.type("#update_name","test_ticket_yo")
        self.type("#update_qty", "20")
        self.type("#update_price","20")
        self.type("#update_date","20210901")

        # click enter button
        self.click('input[type="submit"]')
        # Refresh page
        # validate that the ticket has been updated on user profile page
        self.open(base_url)
