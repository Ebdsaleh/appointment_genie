# controller.py
from src.user.user import User
from src.views.login import Login
from src.views.add_contact import AddContact
from src.views.create_booking import CreateBooking, DateEntry
import src.utils.validators as val


class Controller:
    """
        This class will handle the switch between views and program flow.
    """

    def __init__(self):
        self.user = User.get_instance()
        self.reset_user()
        self.login_view = None
        self.add_contact_view = None
        self.create_booking_view = None

    def handle_login_view(self, title=None):
        if self.login_view is None:
            title = title or "Login"
            self.login_view = Login(controller=self, title=title)
        return self.login_view

    def handle_add_contact_view(self, title=None):
        if self.add_contact_view is None:
            title = title or "Add Contact"
            self.add_contact_view = AddContact(controller=self, title=title)
        return self.add_contact_view

    def handle_create_booking_view(self, title=None):
        if self.create_booking_view is None:
            title = title or "Create Booking"
            self.create_booking_view = CreateBooking(
                    controller=self, title=title)
        return self.create_booking_view

    def handle_login(self, username, password):
        if self.user.authenticate(username, password):
            print("Login successful.")
            return True
        else:
            print("Login failed.")
            return False

    def reset_user(self):
        self.user.reset()

    def handle_add_contact(self, details):
        if details is None:
            raise ValueError("'details' must not be None.")
        for item in details:
            val.validate_string_property(item, 'item in details')
        print(details)
        return True

    def handle_create_booking(self, details):
        if details is None:
            raise ValueError("'details' must not be None.")
        for item in details:
            if isinstance(item, str):
                val.validate_string_property(item, 'item in details')
            if isinstance(item, int):
                val.validate_int_property(item, 'item in details')
        print(details)
        return True


if __name__ == '__main__':
    Controller()
