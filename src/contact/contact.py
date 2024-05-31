# contact.py
import uuid
from src.utils.validators import validate_string_property
from src.user.user import validate_email


class Contact:
    """
    This class will be used to hold contact information for users when making
    bookings.
    attributes:
        _id (uuid) generated during creation and cannot be modified
        _name (str) inputted manually during creation, may be modifid
        _email (str) inputted manually during creation, may be modified
    This class will be expected to raise exceptions when trying to set its
    attributes to incorrect values.
    _id AttributeError: if trying to reassign its value.
    _name ValueError: if None or empty string.
    _name TypeError: if trying set it to a non-string value.
    _email ValueError: if None, empty string or incorrect email format.
    _email TypeError: if trying to set it to a non-string value."""

    def __init__(self, name=None, email=None):
        self._id = uuid.uuid4()
        # assign None values, default values
        if name is None:
            self._name = "New Contact"
        else:
            self._name = name

        if email is None:
            self._email = "unknown@app_genie.app"
        else:
            self._email = email
        print(
                "New Contact Created.\n" +
                f"ID: {self._id}\n" +
                f"Name: {self._name}\n" +
                f"Email: {self._email}\n"
                )

    # Properties
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if self._id is not None:
            raise AttributeError("id attribute is read-only.")
        else:
            self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        validate_string_property(value, 'name')
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        validate_string_property(value, 'email')
        validate_email(value)
        self._email = value
