# test_user.py
import unittest
from src.user.user import User
from src.booking.booking import Booking
from src.contact.contact import Contact
from src.utils.validators import validate_email
from datetime import datetime
from src.utils.auth import generate_pw_hash, verify_password


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()
        self.pw_hash = self.user.password
        self.password = "password"
        self.generic_string_type_error_values = [
                1, 2.2, [2, 3], {}, ()]
        self.generic_string_value_error_values = [None, "", " "]

    def test_create_user_with_default_values(self):
        print("=== test_create_user_with_defaul_values ===")
        # Type assertions
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user.user_name, str)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.contacts, list)
        self.assertIsInstance(self.user.bookings, list)
        self.assertIsInstance(self.user._booking_id, int)
        # Value assertions
        self.assertEqual(self.user.user_name, "new_user")
        self.assertEqual(self.user.email, "update_this_email@appgenie.app")
        self.assertEqual(self.user.password, self.pw_hash)
        self.assertEqual(self.user.contacts, [])
        self.assertEqual(self.user.bookings, [])
        self.assertEqual(self.user._booking_id, 0)

    def test_create_user_with_arguments_success(self):
        print("=== test_create_user_with_arguments_success")
        user = User(
            user_name="test_user",
            email="test_.user@test_email.com",
            password="my_test_password"
            )
        pw_hash = user.password

        # Type assertions
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.user_name, str)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.contacts, list)
        self.assertIsInstance(user.bookings, list)
        self.assertIsInstance(self.user._booking_id, int)

        # Value assertions
        self.assertEqual(user.user_name, "test_user")
        self.assertEqual(user.email, "test_.user@test_email.com")
        self.assertEqual(user.password, pw_hash)
        self.assertEqual(user.contacts, [])
        self.assertEqual(user.bookings, [])
        self.assertEqual(self.user._booking_id, 0)

    def test_create_user_with_arguments_failure_parameter_user_name(self):
        t_name = "test_create_user_with_arguments_failure_parameter_user_name"
        print(f"=== {t_name} ===")
        # need to remove None from the ValueError test because The contsructor
        # already guards against it with a default value.
        raises_value_errors = ["", ' ']
        raises_type_errors = self.generic_string_type_error_values

        # user_name ValueError
        for invalid_value in raises_value_errors:
            with self.subTest(
                    msg="Test values that will raise a ValueError exception " +
                    "for the 'user_name' parameter when creating a new User.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    User(user_name=invalid_value, email=None, password=None)

        # user_name TypeError
        for invalid_value in raises_type_errors:
            with self.subTest(
                    msg="Test values that will raise a TypeError exception " +
                    "for the 'user_name' parameter when creating a new User.",
                    value=invalid_value
                    ):
                with self.assertRaises(TypeError):
                    User(user_name=invalid_value, email=None, password=None)

    def test_create_user_with_arguments_failure_parameter_email(self):
        t_name = "test_create_user_with_arguments_failure_parameter_email"
        print(f"=== {t_name} ===")
        raises_value_errors = ["", ' ']
        raises_type_errors = self.generic_string_type_error_values

        # email ValueError
        for invalid_value in raises_value_errors:
            with self.subTest(
                    msg="Test values that will raise a ValueError exception " +
                    "for the 'email' parameter when creating a new User.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    User(user_name=None, email=invalid_value, password=None)

        # email TypeError
        for invalid_value in raises_type_errors:
            with self.subTest(
                    msg="Test values that will raise a TypeError exception " +
                    "for the 'email' parameter when creating a new User.",
                    value=invalid_value
                    ):
                with self.assertRaises(TypeError):
                    User(user_name=None, email=invalid_value, password=None)

    def test_create_user_with_arguments_failure_parameter_password(self):
        t_name = "test_create_user_with_arguments_failure_parameter_password"
        print(f"=== {t_name} ===")
        raises_value_errors = ["", ' ']
        raises_type_errors = self.generic_string_type_error_values

        # password ValueError
        for invalid_value in raises_value_errors:
            with self.subTest(
                    msg="Test values that will raise a TypeError exception " +
                    "for the 'password' parameter when creating a new User.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    User(user_name=None, email=None, password=invalid_value)

        # password TypeError
        for invalid_value in raises_type_errors:
            with self.subTest(
                    msg="Test values that will raise a TypeError, exception " +
                    "for the 'password' parameter when creating a new User",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    User(None, None, invalid_value)

    def test_contacts_property(self):
        print("=== test_contacts_property ===")

        self.assertIsInstance(self.user.contacts, list)
        contact_name = "new_contact"
        contact_email = "new_contact@email.com"
        new_contact = Contact(contact_name, contact_email)
        self.user.add_contact(new_contact)
        self.assertEqual(
                self.user.contacts, [new_contact])

    def test_get_contacts(self):
        print("=== test_get_contacts ===")
        self.assertIsInstance(self.user.get_contacts(), list)
        self.assertEqual(self.user.get_contacts(), self.user.contacts)

    def test_add_contact(self):
        print("=== test_add_contact ===")

        contact_name = "new_contact"
        contact_email = "new_contact@email.com"
        new_contact = Contact(contact_name, contact_email)
        self.user.add_contact(new_contact)
        self.assertEqual(self.user.contacts, [new_contact])

        raises_value_errors = [None]
        raises_type_errors = [" ", 1.2, 1, [], (), {}]

        # ValueError
        for invalid_value in raises_value_errors:
            with self.subTest(
                    msg="Test the values that raise a ValueError exception " +
                    "for the 'value' parameter in the add_contact method.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.user.add_contact(invalid_value)
        # ValueError
        for invalid_value in raises_type_errors:
            with self.subTest(
                    msg="Test the values that raise a TypeError exception " +
                    "for the 'value' parameter in the add_contact method.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.user.add_contact(invalid_value)

    def test_bookings(self):
        print("=== test_bookings ===")
        self.assertIsInstance(self.user.bookings, list)
        self.assertEqual(self.user.bookings, [])

    def test_create_booking(self):
        print("=== test_create_booking ===")
        title = "New Booking"
        date = datetime(2024, 5, 30)
        time = (12, 30)
        contact_name = "test_contact"
        contact_email = "test_contact@appointment_genie.app"
        new_contact = Contact(contact_name, contact_email)
        self.user.add_contact(new_contact)
        contact_name_1 = "My Friend"
        contact_email_1 = "my_friend@email.com"
        self.user.create_booking(
                title,
                date,
                time,
                contact_name_1,
                contact_email_1,
                desc="Test Booking")

        self.assertEqual(len(self.user.bookings), 1)
        self.assertEqual(self.user._booking_id, 1)
        self.assertEqual(len(self.user.contacts), 2)
        self.assertIsInstance(self.user.contacts[0], Contact)
        self.assertIsInstance(self.user.contacts[1], Contact)

    def tearDown(self):
        self.user = None
        self.pw_hash = None
        self.password = None
        self.generic_string_type_error_values = None


if __name__ == '__main__':
    unittest.main()
