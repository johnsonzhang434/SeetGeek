import pytest
from seleniumbase import BaseCase
from qa327.models import db, User, Ticket
from qa327_test.conftest import base_url
from unittest.mock import patch
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# test ticket data
test_ticket = Ticket(
	name = 'test ticket',
	owner = 1,
	qty = 10,
	price = 15,
	exp = '20211119')

class design_scenarios(BaseCase):
	def test_sell_ticket(self,*_):
		# logout if logged in
		self.open(base_url + '/logout')
		# NOW ON LOGIN PAGE
		# click "Register" to navigate to register page
		self.click("a[href='/register']")
		# NOW ON REGISTER PAGE
		# enter user info into registration form
		self.type("#email", "test_frontend@test.com")
		self.type("#name", "test")
		self.type("#password", "Testing1!")
		self.type("#password2", "Testing1!")
		# click Register button
		self.click('input[type="submit"]')
		# NOW ON LOGIN PAGE
		# validate that there is no error and that we are redirected to /login
		self.assert_text("Please Login", "#message")
		# enter user info into login form
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "Testing1!")
		# click Login button
		self.click('input[type="submit"]')
		# NOW ON HOME PAGE
		# validate that there is no error and that we are redirected to /
		self.assert_text("Hi test !", "#welcome-header")
		# validate that the current page shows a ticket-sell form
		# with test ticket's name, quantity, price, expr date
		self.assert_element("input[name='sell_name']")
		self.assert_element("input[name='sell_qty']")
		self.assert_element("input[name='sell_price']")
		self.assert_element("input[name='sell_date']")
		# Fill ticket info: name, quantity, price, exp date
		self.type("#sell_name","test ticket")
		self.type("#sell_qty", "1")
		self.type("#sell_price","15")
		self.type("#sell_date","20211119")
		# click Sell button
		self.click('input[value="Sell"]')
		# Check to see that the ticket has been posted and no error message appears
		self.assert_text("Ticket Posted for Sale")
		# refresh the page
		self.open(base_url)
		# Check to see that the ticket has been posted and no error message appears
		self.assert_text("test ticket")

	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_purchase_ticket(self,*_):
		# logout if logged in
		self.open(base_url + '/logout')
		# NOW ON LOGIN PAGE
		# click "Register" to navigate to register page
		self.click("a[href='/register']")
		# NOW ON REGISTER PAGE
		# enter user info into registration form
		self.type("#email", "test2_frontend@test.com")
		self.type("#name", "test")
		self.type("#password", "Testing1!")
		self.type("#password2", "Testing1!")
		# click Register button
		self.click('input[type="submit"]')
		# NOW ON LOGIN PAGE
		# validate that there is no error and that we are redirected to /login
		self.assert_text("Please Login", "#message")
		# enter user info into login form
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "Testing1!")
		# click Login button
		self.click('input[type="submit"]')
		# NOW ON HOME PAGE
		# validate that there is no error and that we are redirected to /
		self.assert_text("Hi test !", "#welcome-header")
		# validate that the current page shows a ticket-purchasing form
		# with ticket name and quantity
		self.assert_element("input[name='buy_name']")
		self.assert_element("input[name='buy_qty']")
		# Fill ticket name and quantity
		self.type("#buy_name","test ticket")
		self.type("#buy_qty", "1")
		# click Buy button
		self.click('input[value="Buy"]')
		# Check to see that the ticket has been purchased and no error message appears
		self.assert_text("Ticket Purchased")
		# refresh the page
		self.open(base_url)
		# Check to see that the ticket has been posted and no error message appears
		self.assert_text("test ticket")