# test_contact.py
import unittest
from src.contact.contact import Contact, uuid


class TestContact(unittest.TestCase):

    def setUp(self):
        print("contact setUP")
        self.contact = Contact()

    def test_create_contact_with_default_values(self):
        print("=== test_create_contact_with_default_values ===")
        self.assertIsInstance(self.contact, Contact)
        self.assertIsInstance(self.contact.id, uuid.UUID)
        self.assertIsInstance(self.contact.name, str)
        self.assertIsInstance(self.contact.email, str)

        # Test the values since they're not None and are the correct type
        id = self.contact.id
        self.assertEqual(self.contact.id, id)
        self.assertEqual(self.contact.name, "New Contact")
        self.assertEqual(self.contact.email, "unknown@app_genie.app")

    def test_create_contact_with_non_default_values(self):
        print("=== create_contact_with_non_default_values ===")
        name = "Test Contact"
        email = "test@app_genie.app"
        contact = Contact(name, email)
        self.assertIsInstance(contact, Contact)
        self.assertIsInstance(contact.id, uuid.UUID)
        self.assertIsInstance(contact.name, str)
        self.assertIsInstance(contact.email, str)

        id = contact.id
        self.assertEqual(contact.id, id)
        self.assertEqual(contact.name, "Test Contact")
        self.assertEqual(contact.email, "test@app_genie.app")

    def test_set_name_failure(self):
        print("=== set_name_failure ===")
        # ValueError checks
        raises_value_errors = [None, "", " "]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values which will raise a ValueError exception " +
                "when setting the 'name' property.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.contact.name = invalid_value
        # TypeError checks
        raises_type_errors = [12, 2.0, (), [], {}, uuid.uuid4()]
        for invalid_value in raises_type_errors:
            with self.subTest(
                    msg="Test values which will raise a TypeError exception " +
                    "when setting the 'name' property.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.contact.name = invalid_value

    def test_set_email_failure(self):
        print("=== set_email_failure ===")
        # ValueError checks
        raises_value_errors = [
                None, "", " ", "test._email.com", "bad_email@gmail",
                "not.good.gmail.@", "this_should_fail_too@my_mail.com."]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values which will raise a ValueError exception" +
                "when setting the 'email' property.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.contact.email = invalid_value
        # TypeError checks
        raises_type_errors = [12, 2.0, (), [], {}, uuid.uuid4()]
        for invalid_value in raises_type_errors:
            with self.subTest(
                    msg="Test values which will raise a TypeError execption " +
                    "when setting the 'email' property.", value=invalid_value):
                with self.assertRaises(TypeError):
                    self.contact.email = invalid_value

    def test_set_id_failure(self):
        print("=== test_id_failure ===")
        # This test should prove that the id property cannot be reassigned.
        self.assertIsInstance(self.contact.id, uuid.UUID)
        # AttributeError
        raises_attribute_errors = [
                " ", "", None, uuid.uuid4(), 12, 2.1, (), (1, 2), [],
                [1, 2, 3], {}, {"uuid": "uuid4"}, Contact()
                ]
        for invalid_value in raises_attribute_errors:
            with self.subTest(
                msg="Test values which raise an AttributeError exception " +
                "when setting the 'id' property once contact is created.",
                    value=invalid_value):
                with self.assertRaises(AttributeError):
                    self.contact.id = invalid_value

    def tearDown(self):
        print("contact tearDown")
        self.contact = None


if __name__ == '__main__':
    unittest.main()
