from qa327.models import db, User
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
