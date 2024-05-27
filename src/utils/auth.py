# src/utils/auth/py
from werkzeug.security import check_password_hash, generate_password_hash
from src.utils.validators import is_valid_string

"""
    This module will handle the generating and checking of password hashes.
"""


def generate_pw_hash(password):
    """
        Generate a password hash using Werkzeug.
        Returns the password hash as a string.
    """
    if password is None:
        raise ValueError("'password' must not be None.")
    if not is_valid_string(password):
        if isinstance(password, str) and password.strip() == "":
            raise ValueError("'password' must not be and empty-string.")
        raise TypeError("'password' must be passed in as a string.")
    else:
        return generate_password_hash(
            password=password, method="scrypt", salt_length=16)


def verify_password(pw_hash, password):
    """
        Verify that the password and password hash match.
        Returns True or False.
    """
    # pw_hash validation
    if pw_hash is None:
        raise ValueError("'pw_hash' must not be None.")
    if not is_valid_string(pw_hash):
        if isinstance(pw_hash, str) and pw_hash.strip() == "":
            raise ValueError("'pw_hash' must not be an empty-string.")
        else:
            raise TypeError("'pw_hash' must be passed in as a string.")
    # password validation
    if password is None:
        raise ValueError("'password' must not be None.")
    if not is_valid_string(password):
        if isinstance(password, str) and password.strip() == "":
            raise ValueError("'password' must not be an empty-string.")
        else:
            raise TypeError("'password' must be passed in as a string.")
    return check_password_hash(pw_hash, password)
