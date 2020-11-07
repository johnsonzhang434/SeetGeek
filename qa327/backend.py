from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
import re
"""
This file defines all backend logic that interacts with database and other services
"""
def validate_email(email):
    """
    Validate that email follows RFC 5322
    see stackoverflow for explanation https://stackoverflow.com/questions/201323/how-to-validate-an-email-address-using-a-regular-expression
    """
    return re.fullmatch(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])`'])`'])", email)

def validate_password(password):
    """
    Validate that password is valid
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
    # Validate email and password, then return string explaining errors present
    if not validate_email(email) or not validate_password(password):
        return "Email/password format is incorrect."
    elif not user or not check_password_hash(user.password, password):
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
    new_user = User(email=email, name=name, password=hashed_pw, balance=5000)

    db.session.add(new_user)
    db.session.commit()
    return [] # no errors


def get_all_tickets():
    return []
