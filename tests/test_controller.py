# tests/test_controller.py
import unittest
from src.controller.controller import Controller, Login, User, \
        AddContact, CreateBooking


class TestController(unittest.TestCase):

    def setUp(self):
        print("=== TestController setUp ===")
        self.controller = Controller()

    def test_create_controller(self):
        print("=== test_create_controller ===")
        self.assertIsNotNone(self.controller)
        self.assertIsInstance(self.controller, Controller)
        self.assertIsInstance(self.controller.user, User)
        self.assertEqual(self.controller.login_view, None)
        self.assertEqual(self.controller.add_contact_view, None)
        self.assertEqual(self.controller.create_booking_view, None)

    def test_handle_login(self):
        print("=== test_handle_login ===")
        user_name = "user"
        self.controller.user.user_name = user_name
        from src.utils.auth import generate_pw_hash
        pw_hash = generate_pw_hash('password')
        self.controller.user.password = pw_hash
        self.assertFalse(self.controller.handle_login(user_name, pw_hash))
        self.assertTrue(self.controller.handle_login(user_name, 'password'))

    def test_reset_user(self):
        user_name = "user"
        self.controller.user.user_name = user_name
        from src.utils.auth import generate_pw_hash
        pw_hash = generate_pw_hash('password')
        self.controller.user.password = pw_hash
        self.assertEqual(self.controller.user.user_name, user_name)
        self.assertEqual(self.controller.user.password, pw_hash)
        self.controller.reset_user()
        self.assertEqual(self.controller.user.user_name, str())
        self.assertEqual(self.controller.user.password, str())

    def test_handle_add_contact(self):
        print("=== test_handle_add_contact ===")
        contact_name = "Test Contact"
        contact_email = "test_contact@email.com"
        details = [contact_name, contact_email]
        self.assertTrue(self.controller.handle_add_contact(details))
        with self.assertRaises(ValueError):
            self.controller.handle_add_contact(None)

    def test_handle_create_booking(self):
        print("=== test_handle_create_booking ===")
        contact_name = "test_contact"
        time_tuple = (12, 30)
        hour = time_tuple[0]
        minute = time_tuple[1]
        import datetime
        date = datetime.datetime.now()
        year = date.year
        month = date.month
        day = date.day
        date = datetime.date(year, month, day)
        details = [contact_name, hour, minute, date]
        self.assertTrue(self.controller.handle_create_booking(details))
        with self.assertRaises(ValueError):
            self.controller.handle_create_booking(None)

    def test_handle_login_view(self):
        print("=== test_handle_login_view ===")
        self.assertIsNone(self.controller.login_view)
        self.controller.handle_login_view("test_handle_login_view")
        self.assertIsInstance(self.controller.login_view, Login)
        self.controller.login_view.tk.destroy()

    def test_handle_add_contact_view(self):
        print("=== test_handle_add_contact_view ===")
        self.assertIsNone(self.controller.add_contact_view)
        self.controller.handle_add_contact_view("test_handle_add_contact")
        self.assertIsInstance(self.controller.add_contact_view, AddContact)
        self.controller.add_contact_view.tk.destroy()

    def test_handle_create_booking_view(self):
        print("=== test_handle_create_booking_view ===")
        self.assertIsNone(self.controller.create_booking_view)
        self.controller.handle_create_booking_view(
                "test_handle_create_booking_view")
        self.assertIsInstance(
                self.controller.create_booking_view, CreateBooking)
        self.controller.create_booking_view.tk.destroy()

    def tearDown(self):
        print("=== TestController tearDown ===")
        self.controller.login_view = None
        self.controller.add_contact_view = None
        self.controller.create_booking_view = None
        self.controller = None


if __name__ == '__main__':
    unittest.main()
