
import pytest
from seleniumbase import BaseCase
from qa327.models import db, User, Ticket
from qa327_test.conftest import base_url
from unittest.mock import patch
from werkzeug.security import generate_password_hash, check_password_hash


test_user = User(
	email = 'test_frontend@test.com',
	name = 'test_user',
	password = generate_password_hash('test_frontendA1$')
)
test_ticket = Ticket(
	name = 'test ticket',
	owner = 1,
	qty = 10,
	price = 15,
	exp = '20201119')

class R4Test1(BaseCase):
	@patch('qa327.backend.get_user', return_value=test_user)
	def test_r4_5_2_1(self, *_):
		#logout if logged in
		self.open(base_url + '/logout')
		#login
		self.open(base_url + '/login')
		#enter user credentials
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "test_frontendA1$")

		self.click("input[type='submit']")
		self.open(base_url)
		#make ticket
		self.type("#sell_name", "ticketname")
		self.type("#sell_qty", "10")
		self.type("#sell_price", "15")
		self.type("#sell_date", "abcd")
		#click update
		self.click("#sell")
		self.assert_element("#message")
		self.assert_text("invalid date format")


	@patch('qa327.backend.get_user', return_value=test_user)
	def test_r4_5_2_2(self, *_):
		#logout if logged in
		self.open(base_url + '/logout')
		#login
		self.open(base_url + '/login')
		#enter user credentials
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "test_frontendA1$")

		self.click("input[type='submit']")
		self.open(base_url)
		#make ticket
		self.type("#sell_name", "ticcketname")
		self.type("#sell_qty", "10")
		self.type("#sell_price", "15")
		self.type("#sell_date", "123")
		#click update
		self.click("#sell")
		self.assert_element("#message")
		self.assert_text("invalid date format")


	@patch('qa327.backend.get_user', return_value=test_user)
	def test_r4_7(self, *_):
		#logout if logged in
		self.open(base_url + '/logout')
		#login
		self.open(base_url + '/login')
		#enter user credentials
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "test_frontendA1$")

		self.click("input[type='submit']")
		self.open(base_url)
		#make ticket
		self.type("#sell_name", "ticccketname")
		self.type("#sell_qty", "10")
		self.type("#sell_price", "15")
		self.type("#sell_date", "20201119")
		#click update
		self.click("#sell")
		self.assert_element("#message")
		self.assert_text("ticccketname")
		self.assert_text("10")


	@patch('qa327.backend.get_user', return_value=test_user)
	def test_r5_1(self, *_):
		#logout if logged in
		self.open(base_url + '/logout')
		#login
		self.open(base_url + '/login')
		#enter user credentials
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "test_frontendA1$")

		self.click("input[type='submit']")
		self.open(base_url)
		#enter new name/updated name
		self.type("#sell_name", "  leading and trailing spaces  ")
		self.type("#sell_qty", "10")
		self.type("#sell_price", "15")
		self.type("#sell_date", "20201119")
		#click update
		self.click("#sell")
		self.assert_element("#message")
		self.assert_text("Ticket name cannot begin/end with a space")


	@patch('qa327.backend.get_user', return_value=test_user)
	def test_r5_2(self, *_):
		#logout if logged in
		self.open(base_url + '/logout')
		#login
		self.open(base_url + '/login')
		#enter user credentials
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "test_frontendA1$")

		self.click("input[type='submit']")
		self.open(base_url)
		#enter new name/updated name
		self.type("#sell_name", "11234567890123456789012345678901234567890123456789012345678901234567890")
		self.type("#sell_qty", "10")
		self.type("#sell_price", "15")
		self.type("#sell_date", "20201119")
		#click update
		self.click("#sell")
		self.assert_element("#message")
		self.assert_text("Ticket name exceeds character limit (60)")


	@patch('qa327.backend.get_user', return_value=test_user)
	def test_r5_3_1(self, *_):
		#logout if logged in
		self.open(base_url + '/logout')
		#login
		self.open(base_url + '/login')
		#enter user credentials
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "test_frontendA1$")

		self.click("input[type='submit']")
		self.open(base_url)
		#enter new name/updated name
		self.type("#sell_name", "tickettet")
		self.type("#sell_qty", "0")
		self.type("#sell_price", "15")
		self.type("#sell_date", "20201119")
		#click update
		self.click("#sell")
		self.assert_element("#message")
		self.assert_text("Ticket quantity must be greater than (0)")


	@patch('qa327.backend.get_user', return_value=test_user)
	def test_r5_3_2(self, *_):
		#logout if logged in
		self.open(base_url + '/logout')
		#login
		self.open(base_url + '/login')
		#enter user credentials
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "test_frontendA1$")

		self.click("input[type='submit']")
		self.open(base_url)
		#enter new name/updated name
		self.type("#sell_name", "tickettett")
		self.type("#sell_qty", "101")
		self.type("#sell_price", "15")
		self.type("#sell_date", "20201119")
		#click update
		self.click("#sell")
		self.assert_element("#message")
		self.assert_text("Maxiumum ticket quantity is (100)")


	@patch('qa327.backend.get_user', return_value=test_user)
	def test_r5_4_1(self, *_):
		#logout if logged in
		self.open(base_url + '/logout')
		#login
		self.open(base_url + '/login')
		#enter user credentials
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "test_frontendA1$")

		self.click("input[type='submit']")
		self.open(base_url)
		#enter new name/updated name
		self.type("#sell_name", "tickettettt")
		self.type("#sell_qty", "10")
		self.type("#sell_price", "9")
		self.type("#sell_date", "20201119")
		#click update
		self.click("#sell")
		self.assert_element("#message")
		self.assert_text("Ticket price must be at least $10")


	@patch('qa327.backend.get_user', return_value=test_user)
	def test_r5_4_2(self, *_):
		#logout if logged in
		self.open(base_url + '/logout')
		#login
		self.open(base_url + '/login')
		#enter user credentials
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "test_frontendA1$")

		self.click("input[type='submit']")
		self.open(base_url)
		#enter new name/updated name
		self.type("#sell_name", "tickettett")
		self.type("#sell_qty", "10")
		self.type("#sell_price", "101")
		self.type("#sell_date", "20201119")
		#click update
		self.click("#sell")
		self.assert_element("#message")
		self.assert_text("Maximum ticket price is $100")
