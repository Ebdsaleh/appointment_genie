# src/user/user.py
from src.utils.validators import validate_string_property, \
        validate_string_dict_property
from src.utils.auth import check_password_hash, generate_pw_hash
from src.booking.booking import Booking


def validate_email(email):
    """
        This function validates an email by checking for '@' and '.' in the
        'email' string passed in.
        If both symbols exist then it checks for multiple occurances of a '.',
        if there is more than one occurance it checks their positions.

        For a valid email:
        The '.' is not the last character in the 'email' string and the last
        '.' must be in a greater position than the '@'.

        parameters: email: str
        raises: ValueError, TypeError (via validate_string_property)
    """
    validate_string_property(email, 'email')
    is_email_OK = False
    if '@' in email and '.' in email:
        at_index = email.find('@')
        dot_index = email.find('.')
        dot_pos = dot_index

        if email.count('.') > 1:
            for i in range(dot_pos, len(email)):
                if email[i] == '.':
                    dot_index = i

        if dot_index != len(email) - 1 and dot_index > at_index:
            is_email_OK = True
        else:
            is_email_OK = False
    if not is_email_OK:
        raise ValueError("Invalid 'email' format.")


class User:
    """
    This class will create a new User object with:
        user_name : str,
        password : str (stored as a password hash),
        email : str,
        contacts : list of Contact objects.
    """
    _booking_id = 0

    def __init__(self, user_name=None, email=None, password=None):
        if user_name is None:
            self.user_name = "new_user"
        else:
            validate_string_property(user_name, 'user_name')
            self.user_name = user_name

        if email is None:
            self.email = "update_this_email@appgenie.app"
        else:
            validate_email(email)
            self.email = email

        if password is None:
            self.password = generate_pw_hash("password")
        else:
            validate_string_property(password, 'password')
            self.password = generate_pw_hash(password)

        self.contacts = []
        self.bookings = []

    def get_contacts(self):
        return self.contacts

    def add_contact(self, value):
        if value is None:
            raise ValueError("contact must not be None.")
        from src.contact.contact import Contact
        if not isinstance(value, Contact):
            raise TypeError("'contact' must be a of type 'Contact'")
        else:
            self.contacts.append(value)

    def create_booking(
            self,
            title,
            date,
            time,
            contact_name,
            contact_email,
            desc):
        booking = Booking()
        booking.title = title
        booking.date = date
        booking.time = time
        booking.contact = contact_name
        booking.description = desc
        self._booking_id += 1
        self.bookings.append(booking)
        contact_found = False

        from src.contact.contact import Contact
        for item in self.contacts:
            if contact_name in item.name:
                if contact_email in item.email:
                    contact_found = True
        if not contact_found:
            print(f"{contact_name} not found in contact list. " +
                  "Adding them to your contacts.")
            new_contact = Contact(contact_name, contact_email)
            self.add_contact(new_contact)
        print(f"sending email to {contact_email}to confirm booking")
