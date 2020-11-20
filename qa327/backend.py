from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
from email_validator import validate_email as val_e, EmailNotValidError

"""
This file defines all backend logic that interacts with database and other services
"""
def validate_email(email):
	"""
	Validate that email follows RFC 5322
	:param email: email to be validated
	:return: boolean, valid or not
	"""
	try:
		val_e(email)
		return True
	except EmailNotValidError as e :
		return False


def validate_password(password):
	"""
	Validate that password is valid
	:param password: password to be validated
	:return: boolean, valid or not
	"""
	# min length 6
	if len(password) < 6:
		return False
	# at least one upper and one lower
	if password.isupper() or password.islower():
		return False
	# any special character
	return any(c for c in password if not c.isalnum() and not c.isspace())

def validate_username(name):
	"""
	Validate that name is valid
	:param name: name to be validated
	:return: boolean, valid or not
	"""
	# not empty
	if len(name) <= 2 or len(name) >= 20:
		return False
	# alpha numerico only
	if any(not (x.isalnum() or x.isspace()) for x in name):
		return False
	# space not firs or last
	if name[0] == " " or name[-1] == " ":
		return False
	return True

def get_user(email):
	"""
	Get a user by a given email
	:param email: the email of the user
	:return: a user that has the matched email address
	"""
	user = User.query.filter_by(email=email).first()
	return user

def login_user(email, password):
	"""
	Check user authentication by comparing the password
	:param email: the email of the user
	:param password: the password input
	:return: the user if login succeeds
	"""
	# if this returns a user, then the name already exists in database
	user = get_user(email)
	# Validate email and password, then return string explaining errors present
	if not validate_email(email) or not validate_password(password):
		return "Email/password format is incorrect."
	elif not user or not user.email == email or  not check_password_hash(user.password, password):
		return None
	return user


def register_user(email, name, password, password2):
	"""
	Register the user to the database
	:param email: the email of the user
	:param name: the name of the user
	:param password: the password of user
	:param password2: another password input to make sure the input is correct
	:return: an error message if there is any, or None if register succeeds
	"""
	errors = []
	# checks if email is valid format
	if not validate_email(email):
		errors.append("email format is incorrect")
	# checks if password is valid format
	if not validate_password(password):
		errors.append("password format is incorrect")
	# checks if passwords match
	if password != password2:
		errors.append("passwords do not match")
	# chechs if username has valid formats
	if not validate_username(name):
		errors.append("username format is incorrect")
	# check if email has been used before
	user = get_user(email)
	if user:
		errors.append("this email has been ALREADY used")
	# generate password hash
	hashed_pw = generate_password_hash(password, method='sha256')
	# do not create user if there are any errorsx
	if len(errors) > 0:
		return errors

	# store the encrypted password rather than the plain password
	new_user = User(email=email, name=name, password=hashed_pw, balance=5000.0)

	db.session.add(new_user)
	db.session.commit()
	return [] # no errors


def get_all_tickets():
	return []

def validate_ticket_name(name):
	"""
	validate that the ticket name is valid
	:param name: the name of the ticket
	:return: an error message (if any) or nothing if the ticket name is in the correct format
	"""
	errors = []
	#name cannot be empty
	if len(name) <= 0:
		errors.append("Ticket name must contain at least (1) character")
	#name must be alphanumeric
	if not all(n.isalnum() or n.isspace() for n in name):
		errors.append("Ticket name must be alphanumeric only")
	#cannot have leading/trailing spaces
	if len(name) != 0 and (name[0] == ' ' or name[-1] == ' '):
		errors.append("Ticket name cannot begin/end with a space")
	#name has a max of 60 characters
	if len(name) > 60:
		errors.append("Ticket name exceeds character limit (60)")
	return errors


def validate_ticket_qty(qty):
	"""
	validate that the ticket quantity is between 1 and 100 (inclusive)
	:param qty: the qty of tickets
	:return: an error message (if any) or nothing if the quantity is valid
	"""
	errors = []
	if int(qty) <= 0:
		errors.append("Ticket quantity must be greater than (0)")
	if int(qty) > 100:
		errors.append("Maxiumum ticket quantity is (100)")
	return errors


def validate_ticket_price(price):
	"""
	validate that the ticket price is between $10 and $100 (inclusive)
	:param price: price of the ticket
	:return: an error message (if any) or nothing if the price is valid
	"""

	errors = []
	if int(price) < 10:
		errors.append("Ticket price must be at least $10")
	if int(price) > 100:
		errors.append("Maximum ticket price is $100")
	return errors


def validate_ticket_date(date):
	"""
	validate that the date is in YYYYMMDD format
	:param date: date of the ticket
	:return: True if valid, False otherwise
	"""
	year = date[0:4]
	month = date[4:6]
	day = date[6:-1]
	if len(date) != 8:
		return False
	if not date.isnumeric():
		return False
	if int(year) < 2000 or int(year) > 3000:
		return False
	if int(month) < 1 or int(month) > 12:
		return False
	if int(day) < 1 or int(day) > 31:
		return False
	return True


def get_ticket(ticket):
	"""
	validate that the ticket being updated already exists in database
	:param ticket: is the ticket name being checked if it is in the database
	:return: True if found in db, False otherwise
	"""
	ticket = Ticket.query.filter_by(name=ticket).first()
	return ticket


def update_ticket(orig_name, new_name, qty, price, date):
	"""
	heck
	"""
	errors = []
	if get_ticket(orig_name) is None:
		errors.append("Ticket not found, ticket not updated")
	errors += (validate_ticket_name(new_name))
	errors += (validate_ticket_qty(qty))
	errors +=(validate_ticket_price(price))
	if not validate_ticket_date(date):
		errors.append("invalid date format")

	if len(errors) > 0:
		return errors

	#update db here
	#check_ticket_in_db(orig_name) = Ticket(new_name, qty, price, date)
	return []


def calculate_price(p, q):
	price = int(p)
	qty = int(q)
	service_fee = 5
	tax = 1.13
	return int(price * qty * tax + service_fee)

def validate_buy_price(ticket_price, balance, qty):
	if calculate_price(ticket_price, qty) < balance:
		return []
	return ["Insufficient balance"]

def validate_buy_qty(qty, buy_qty):
	if int(qty) <= buy_qty:
		return []
	return ["Invalid purchase quantity"]


def buy_ticket(name, qty, user):
	errors = []
	if get_ticket(name) is None:
		errors.append("Ticket does not exist")
	else:
		ticket = get_ticket(name)
		buy_qty = ticket.qty
		price = ticket.price
		errors += (validate_ticket_name(name))
		errors += (validate_ticket_qty(qty))
		errors += (validate_buy_qty(qty, buy_qty))
		errors +=(validate_buy_price(price, user.balance, qty))

	if len(errors) > 0:
		return errors

	return []
