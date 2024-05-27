# src/utils/validators.py
from datetime import datetime


# Generic validators
def is_valid_string(value):
    """
    Returns True if a string is valid, otherwise returns False.
    """
    return isinstance(value, str) and value.strip() != ""


def is_valid_datetime(value):
    """
    Returns True if a datetime object is valid, otherwise returns False.
    """
    return isinstance(value, datetime)


def is_valid_int(value):
    """
    Returns True if an int is valid otherwise returns False.
    """
    return isinstance(value, int)


def is_valid_tuple(value):
    """
    Returns True if a tuple is valid otherwise returns False.
    """
    return isinstance(value, tuple)


def is_valid_dict(value):
    """
    Returns True if a dict is valid otherwise returns False.
    """
    return isinstance(value, dict)


def validate_string_property(value, property_name):
    if value is None:
        raise ValueError(f"'{property_name}' must not be None.")

    elif property_name is None:
        raise ValueError("'property_name' must not be None.")

    if not is_valid_string(value):
        if isinstance(value, str) and value.strip() == "":
            raise ValueError(f"'{property_name}' must not be an empty-string")
        else:
            raise TypeError(f"'{property_name}' must be a string.")

    if not is_valid_string(property_name):
        if isinstance(property_name, str) and property_name.strip() == "":
            raise ValueError("'property_name' must not be an empty-string.")
        else:
            raise TypeError("'property_name' must be a string.")


def validate_datetime_property(value, property_name):
    if value is None:
        raise ValueError(f"{property_name} must not be None.")

    elif property_name is None:
        raise ValueError("'property_name' must not be None.")

    elif not is_valid_string(property_name):
        if isinstance(property_name, str) and property_name.strip() == "":
            raise ValueError("'property_name' must not be an empty-string.")
        else:
            raise TypeError("'property_name' must be a string.")

    if not is_valid_datetime(value):
        raise TypeError(f"{property_name} must be a datetime value")


def validate_int_tuple_property(value, property_name):
    if value is None:
        raise ValueError(f"{property_name}, must not be None.")

    if not is_valid_tuple(value):
        raise TypeError(f"{property_name}, must be an int tuple.")

    if len(value) == 0:
        raise ValueError(f"{property_name}, must not be empty.")

    if property_name is None:
        raise ValueError("'property_name' must not be None.")

    if not is_valid_string(property_name):
        if isinstance(property_name, str) and property_name.strip() == "":
            raise ValueError("'property_name' must not be an empty-string.")
        else:
            raise TypeError("'property_name' must be a string.")

    for x in value:
        if not isinstance(x, int):
            raise TypeError(
                f"{property_name}, must only contain int values.")


def validate_dict_property(value: dict, property_name: str):
    validate_string_property(property_name, property_name)
    if value is None:
        raise ValueError("'dict' must not be None.")

    if is_valid_dict(value) and len(value) == 0:
        raise ValueError(f"'{property_name}' can not be an empty-dict.")

    if not is_valid_dict(value):
        raise TypeError(f"{property_name} must be a 'dict'.")

    for k, v in value.items():
        if not isinstance(k, str):
            raise ValueError(f"{property_name}'s key must be a string.")
        if not isinstance(v, str):
            raise ValueError(f"{property_name}'s value must be a string.")

