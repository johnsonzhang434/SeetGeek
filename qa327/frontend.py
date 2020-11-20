from flask import render_template, request, session, redirect, url_for
from functools import wraps

from qa327 import app
from qa327.models import db, Ticket
import qa327.backend as bn
import datetime
"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder.
"""


@app.route('/register', methods=['GET'])
def register_get():
	# if user has logged in, redirect back to the user profile page /
	if 'logged_in' in session:
		return redirect('/')
	# else show the user registration page
	return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
	email = request.form.get('email')
	name = request.form.get('name')
	password = request.form.get('password')
	password2 = request.form.get('password2')

	# get the List of errors returned from the backend function: register_user
	# store the returned list in elist
	elist = bn.register_user(email, name, password, password2)

	# if there is any error messages when registering new user
	# at the backend, redirect user to login page
	# display the first error message on the login page.
	if len(elist) > 0:
		return redirect(url_for('.login_get', msg=elist[0]))
	else:
		return redirect(url_for('.login_get', msg='Please Login'))

@app.route('/login', methods=['GET'])
def login_get():
	# redirect to home page or login page, depending on whether user is or isn't already logged in
	# Get any messages passed through this route and store in msg
	msg = request.args.get('msg')
	#if there are any error messages, display them
	if msg:
		return render_template('login.html', message=msg)
	if 'logged_in' in session:
		return redirect('/')
	return render_template('login.html', message='Please Login')


@app.route('/login', methods=['POST'])
def login_post():
	email = request.form.get('email')
	password = request.form.get('password')
	user = bn.login_user(email, password)

	# If login_user() returns a string
	if isinstance(user, str):
		return render_template('login.html', message=user) # return error message

    # email and password are non-empty
	if user:
		session['logged_in'] = user.email
		"""
		Session is an object that contains sharing information
		between browser and the end server. Typically it is encrypted
		and stored in the browser cookies. They will be past
		along between every request the browser made to this services.

		Here we store the user object into the session, so we can tell
		if the client has already login in the following sessions.

		"""
		# success! go back to the home page
		# code 303 is to force a 'GET' request
		return redirect('/', code=303)
	else:
		# if error present in email or password, return list of errors
		return render_template('login.html', message='Email/password combination incorrect')


@app.route('/logout')
def logout():
	if 'logged_in' in session:
		session.pop('logged_in', None)
	return redirect('/')


def authenticate(inner_function):
	"""
	:param inner_function: any python function that accepts a user object

	Wrap any python function and check the current session to see if
	the user has logged in. If login, it will call the inner_function
	with the logged in user object.

	To wrap a function, we can put a decoration on that function.
	Example:

	@authenticate
	def home_page(user):
		pass
	"""
	@wraps(inner_function)
	def wrapped_inner():

		# check did we store the key in the session
		if 'logged_in' in session:
			email = session['logged_in']
			user = bn.get_user(email)
			if user:
				# if the user exists, call the inner_function
				# with user as parameter
				return inner_function(user)
		else:
			# else, redirect to the login page
			return redirect('/login')

	# return the wrapped version of the inner_function:
	return wrapped_inner

#If any other redirects are made other than: /logout, /, /register, /login,
#/sell, /buy,/update, then Redirect to 404 error page
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', message='404 Error')


@app.route('/')
@authenticate
def profile(user):
	# authentication is done in the wrapper function
	# see above.
	# by using @authenticate, we don't need to re-write
	# the login checking code all the time for other
	# front-end portals
	tickets = bn.get_all_tickets()
  return render_template('index.html', user=user, tickets=tickets, balance=user.balance)


@app.route('/update', methods = ['POST'])
@authenticate
def update_post(user):
	"""
	"""
	orig_name = request.form.get('orig_name')
	update_name = request.form.get('update_name')
	qty = request.form.get('update_qty')
	price = request.form.get('update_price')
	date = request.form.get('update_date')
	error_list = []
	error_list = bn.update_ticket(orig_name, update_name, qty, price, date)

	if len(error_list) >0:
		return render_template('index.html', user = user, tickets=tickets, balance=user.balance message = error_list[0])
	else:
		return render_template('index.html', user = user, tickets=tickets, balance=user.balance message = 'Ticket Updated')


@app.route('/buy', methods=['POST'])
@authenticate
def buy_post(user):

	buy_name = request.form.get('buy_name')
	qty = request.form.get('buy_qty')
	error_list = []
	error_list = bn.buy_ticket(buy_name, qty, user)

	if len(error_list) >0:
		return render_template('index.html', user = user, tickets=tickets, balance=user.balance message = error_list[0])
	else:
		return render_template('index.html', user = user, tickets=tickets, balance=user.balance message = 'Ticket Purchased')
