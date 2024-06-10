# src/user/user.py
from src.utils.validators import validate_string_property, \
        validate_string_dict_property, validate_email
from src.utils.auth import check_password_hash, generate_pw_hash
from src.contact.contact import Contact
from src.booking.booking import Booking


class User:
    """
    This class will create a new User object with:
        user_name : str,
        password : str (stored as a password hash),
        email : str,
        contacts : list of Contact objects.
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(User, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

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
        self._initialized = True  # Avoids re-initializing

    def get_contacts(self):
        return self.contacts

    def add_contact(self, value):
        if value is None:
            raise ValueError("contact must not be None.")
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

    @classmethod
    def get_instance(cls):
        """
            Gets the running instance of the User, or creates a new instance if
            none exists.
        """
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance
