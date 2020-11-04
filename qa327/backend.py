from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all backend logic that interacts with database and other services
"""
def validate_email(email):
    """
    Validate that email follows RFC 5322
    """
    return True

def validate_password(password):
    """
    Validate that password is valid
    """
    return True

def validate_username(name):
    """
    Validate that password is valid
    """
    # not empty 
    if len(name) <= 0:
        return False
    # alpha numerico only
    if not name.isalnum():
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
    if not user or not check_password_hash(user.password, password):
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

    if not validate_email(email):
        errors.add("email format is incorrect")

    if not validate_password(password):
        errors.add("password format is incorrect")

    if password != password2:
        errors.add("passwords do not match")

    if not validate_username(name):
        errors.add("username format is incorrect")

    user = bn.get_user(email)
    if user:
        errors.add("this email has been ALREADY used")

    hashed_pw = generate_password_hash(password, method='sha256')

    if len(errors) > 0:
        return errors

    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw, balance=5000)

    db.session.add(new_user)
    db.session.commit()
    return errors


def get_all_tickets():
    return []
