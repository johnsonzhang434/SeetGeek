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
	# R4.1.1: Check if the selling actions succeed when the ticket name is alphanumeric only
	def test_r4_1_1(self,*_):
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
		self.type("#sell_name","testticket") #alphanumeric ticket name
		self.type("#sell_qty", "1")
		self.type("#sell_price","10")
		self.type("#sell_date","20210901")
		# click Sell button
		self.click('input[value="Sell"]')

		# Check to see that the ticket has been posted and no error message appears
		self.assert_text("Ticket Posted for Sale")
		# refresh the page
		self.open(base_url)
		# Check to see that the ticket has been posted and no error message appears
		self.assert_text("testticket")

	@patch('qa327.backend.get_user', return_value=test_user)
	# R4.1.2: Check if the selling actions fail when the ticket name contains special characters
	def test_r4_1_2(self,*_):
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
		self.type("#sell_name","ticketname!^&*") # ticket name contains special characters
		self.type("#sell_qty", "1")
		self.type("#sell_price","10")
		self.type("#sell_date","20210901")
		# click Sell button
		self.click('input[value="Sell"]')

		#Check to see that the ticket has not been posted and error message appears
		self.assert_text("Ticket name must be alphanumeric only")

	@patch('qa327.backend.get_user', return_value=test_user)
	# R4.1.3: Check if the selling actions succeed when the ticket 
	# name uses a space somewhere other than the beginning or end
	def test_r4_1_3(self,*_):
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
		self.type("#sell_name","test ticket") # space within ticket name
		self.type("#sell_qty", "1")
		self.type("#sell_price","10")
		self.type("#sell_date","20210901")
		# click Sell button
		self.click('input[value="Sell"]')

		# Check to see that the ticket has been posted and no error message appears
		self.assert_text("Ticket Posted for Sale")
		# refresh the page
		self.open(base_url)
		# Check to see that the ticket has been posted and no error message appears
		self.assert_text("test ticket")

	@patch('qa327.backend.get_user', return_value=test_user)
	# R4.1.4: Check if the selling actions fail when the ticket 
	# name uses a space at the beginning or end
	def test_r4_1_4(self,*_):
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
		self.type("#sell_name"," testticket ") # ticket name contains leading/trailing spaces
		self.type("#sell_qty", "1")
		self.type("#sell_price","10")
		self.type("#sell_date","20210901")
		# click Sell button
		self.click('input[value="Sell"]')

		#Check to see that the ticket has not been posted and error message appears
		self.assert_text("Ticket name cannot begin/end with a space")

	@patch('qa327.backend.get_user', return_value=test_user)
	# R4.2.1: Check if the selling actions succeed when the 
	# ticket name is 60 characters or less
	def test_r4_2_1(self,*_):
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
		self.type("#sell_name","testticket") # ticket name < 60 characters
		self.type("#sell_qty", "1")
		self.type("#sell_price","10")
		self.type("#sell_date","20210901")
		# click Sell button
		self.click('input[value="Sell"]')

		# Check to see that the ticket has been posted and no error message appears
		self.assert_text("Ticket Posted for Sale")
		# refresh the page
		self.open(base_url)
		# Check to see that the ticket has been posted and no error message appears
		self.assert_text("testticket")

	@patch('qa327.backend.get_user', return_value=test_user)
	# R4.2.2: Check if the selling actions fail when 
	# the ticket name is greater than 60 characters
	def test_r4_2_2(self,*_):
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
		self.type("#sell_name","testtickettesttickettesttickettesttickettesttickettesttickettestticket") # ticket name > 60 characters
		self.type("#sell_qty", "1")
		self.type("#sell_price","10")
		self.type("#sell_date","20210901")
		# click Sell button
		self.click('input[value="Sell"]')

		#Check to see that the ticket has not been posted and error message appears
		self.assert_text("Ticket name exceeds character limit (60)")

	@patch('qa327.backend.get_user', return_value=test_user)
	# R4.3.1: Check if the selling actions succeed when the 
	# ticket quantity is greater than 0 and less than 101
	def test_r4_3_1(self,*_):
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
		self.type("#sell_qty", "10") # ticket quantity between 0 and 101
		self.type("#sell_price","10")
		self.type("#sell_date","20210901")
		# click Sell button
		self.click('input[value="Sell"]')

		# Check to see that the ticket has been posted and no error message appears
		self.assert_text("Ticket Posted for Sale")
		# refresh the page
		self.open(base_url)
		# Check to see that the ticket has been posted and no error message appears
		self.assert_text("testticket")