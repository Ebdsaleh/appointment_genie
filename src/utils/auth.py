# src/utils/auth/py
from werkzeug.security import check_password_hash, generate_password_hash
from src.utils.validators import validate_string_property

"""
    This module will handle the generating and checking of password hashes.
"""


def generate_pw_hash(password):
    """
        Generate a password hash using Werkzeug.
        Returns the password hash as a string.
    """
    validate_string_property(password, 'password')
    return generate_password_hash(
            password=password, method="scrypt", salt_length=16)


def verify_password(pw_hash, password):
    """
        Verify that the password and password hash match.
        Returns True or False.
    """
    # pw_hash validation
    validate_string_property(pw_hash, 'pw_hash')
    # password validation
    validate_string_property(password, 'password')
    return check_password_hash(pw_hash, password)
