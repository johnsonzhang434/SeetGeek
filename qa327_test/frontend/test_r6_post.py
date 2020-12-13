import pytest
from seleniumbase import BaseCase
from qa327.models import db, User, Ticket
from qa327_test.conftest import base_url
from unittest.mock import patch
from werkzeug.security import generate_password_hash, check_password_hash


test_user = User(
	email = 'test_frontend@test.com',
	name = 'test_user',
	password = generate_password_hash('test_frontendA1$'),
	balance = 100)

test_user2 = User(
	email = 'test_frontend@test.com',
	name = 'test_user',
	password = generate_password_hash('test_frontendA1$'),
	balance = 5000)
 
test_ticket = Ticket(
	name = 'test ticket',
	owner = 1,
	qty = 100,
	price = 1,
	exp = '20201119')

test_ticket2 = Ticket(
	name = 'test ticket',
	owner = 1,
	qty = 10,
	price = 15,
	exp = '20201119')

test_ticket3 = Ticket(
	name = 'test ticket 3',
	owner = 1,
	qty = 100,
	price = 10,
	exp = '20201207')

test_ticket4 = Ticket(
	name = 'test ticket 4',
	owner = 1,
	qty = 10,
	price = 15,
	exp = '20201119')


class R6Test(BaseCase):
	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_1a(self, *_):
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
		self.type("#buy_name", "  leading and trailing spaces  ")
		self.type("#buy_qty", "10")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket name cannot begin/end with a space")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_1b(self, *_):
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
		self.type("#buy_name", "ticket1 @#$")
		self.type("#buy_qty", "10")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket name must be alphanumeric only")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_1c(self, *_):
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
		self.type("#buy_name", ",.,.,.,.,.,.$#%#!#%#")
		self.type("#buy_qty", "10")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket name must be alphanumeric only")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_1d(self, *_):
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
		self.type("#buy_name", "ticket1")
		self.type("#buy_qty", "10")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket Purchased")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_1e(self, *_):
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
		self.type("#buy_name", "ticket 1")
		self.type("#buy_qty", "10")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket Purchased")



	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_2a(self, *_):
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
		self.type("#buy_name", "abcdegfhijklmnopqrstuvwxyzabcdegfhijklmnopqrstuvwxyzabcdegfhijklmnopqrstuvwxyz")
		self.type("#buy_qty", "10")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket name exceeds character limit (60)")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_2b(self, *_):
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
		self.type("#buy_name", "")
		self.type("#buy_qty", "10")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket name must contain at least (1) character")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_2c(self, *_):
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
		self.type("#buy_name", "                                                             ")
		self.type("#buy_qty", "10")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket name cannot begin/end with a space")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_2d(self, *_):
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
		self.type("#buy_name", "abcdefghijklmnopqrstuvwxyz aaaaaaaaaaaaabbbbbbbbbbcccccccccc")
		self.type("#buy_qty", "10")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket Purchased")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_3a(self, *_):
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
		self.type("#buy_name", "test ticket")
		self.type("#buy_qty", "0")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket quantity must be greater than (0)")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_3b(self, *_):
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
		self.type("#buy_name", "test ticket")
		self.type("#buy_qty", "-4")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket quantity must be greater than (0)")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_3c(self, *_):
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
		self.type("#buy_name", "test ticket")
		self.type("#buy_qty", "101")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Maxiumum ticket quantity is (100)")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket)
	def test_r6_3d(self, *_):
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
		self.type("#buy_name", "test ticket")
		self.type("#buy_qty", "10")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket Purchased")

	@patch('qa327.backend.get_user', return_value=test_user2)
	@patch('qa327.backend.get_ticket', return_value=test_ticket3)
	def test_r6_3e(self, *_):
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
		self.type("#buy_name", "test ticket")
		self.type("#buy_qty", "99")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket Purchased")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket2)
	def test_r6_4a(self, *_):
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
		self.type("#buy_name", "test ticket")
		self.type("#buy_qty", "11")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Invalid purchase quantity")

	@patch('qa327.backend.get_user', return_value=test_user2)
	@patch('qa327.backend.get_ticket', return_value=test_ticket2)
	def test_r6_4b(self, *_):
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
		self.type("#buy_name", "test ticket")
		self.type("#buy_qty", "4")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket Purchased")

	@patch('qa327.backend.get_user', return_value=test_user)
	def test_r6_4c(self, *_):
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
		self.type("#buy_name", "test ticket")
		self.type("#buy_qty", "4")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket does not exist")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket2)
	def test_r6_5a(self, *_):
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
		self.type("#buy_name", "test ticket")
		self.type("#buy_qty", "1")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Ticket Purchased")

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_ticket', return_value=test_ticket4)
	def test_r6_5b(self, *_):
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
		self.type("#buy_name", "test ticket")
		self.type("#buy_qty", "10")
		#click update
		self.click("#buy")
		self.assert_element("#message")
		self.assert_text("Insufficient balance")
