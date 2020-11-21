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

class R5Test(BaseCase):
	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_1a(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "  leading and trailing spaces  ")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket name cannot begin/end with a space")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_1b(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "ticket1 @#$")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket name must be alphanumeric only")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_1c(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", ",.,.,.,.,.,.$#%#!#%#")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket name must be alphanumeric only")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_1d(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "ticket1")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket Updated")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_1e(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "ticket 1")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket Updated")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_2a(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "abcdegfhijklmnopqrstuvwxyzabcdegfhijklmnopqrstuvwxyzabcdegfhijklmnopqrstuvwxyz")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket name exceeds character limit (60)")


	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_2b(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket name must contain at least (1) character")


	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_2c(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "                                                             ")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket name cannot begin/end with a space")


	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_2d(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "abcdefghijklmnopqrstuvwxyz aaaaaaaaaaaaabbbbbbbbbbcccccccccc")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket Updated")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_3a(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "0")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket quantity must be greater than (0)")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_3b(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "-4")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket quantity must be greater than (0)")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_3c(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "101")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Maxiumum ticket quantity is (100)")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_3d(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "1")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket Updated")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_3e(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "100")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket Updated")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_4a(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "1")
		self.type("#update_price", "0")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket price must be at least $10")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_4b(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "10")
		self.type("#update_price", "9")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket price must be at least $10")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_4c(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "10")
		self.type("#update_price", "-10")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket price must be at least $10")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_4d(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "10")
		self.type("#update_price", "101")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Maximum ticket price is $100")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_4e(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "10")
		self.type("#update_price", "10")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket Updated")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_4f(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "10")
		self.type("#update_price", "100")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket Updated")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_5a(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "03312020")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("invalid date format")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_5b(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20203104")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("invalid date format")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_5c(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20201031")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket Updated")

	@patch('qa327.backend.get_user', return_value=test_user)
	def test_r5_6a(self, *_):
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
		self.type("#orig_name", "test ticket 1")
		self.type("#update_name", "test ticket")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket not found, ticket not updated")


	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r5_6b(self, *_):
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
		self.type("#orig_name", "test ticket")
		self.type("#update_name", "test ticket 1")
		self.type("#update_qty", "10")
		self.type("#update_price", "15")
		self.type("#update_date", "20201119")
		#click update
		self.click("#update")
		self.assert_element("#message")
		self.assert_text("Ticket Updated")
