import unittest
import tkinter as tk
import tkinter.ttk as ttk
from src.views.add_contact import AddContact
from src.views.view import View


class MockController:
    def handle_add_contact(self, details):
        self.details = details


class TestViewAddContact(unittest.TestCase):

    def setUp(self):
        print("=== setUp TestViewAddContact ===")
        self.controller = MockController()
        self.view_add_contact = AddContact(controller=self.controller)
        self.component_names = [
               name for component in self.view_add_contact.components
               for name in component.keys()]
        self.widgets = [
                ttk.Frame, ttk.Label, ttk.Label, ttk.Label, tk.Entry, tk.Entry,
                tk.Button, tk.Button]

    def test_create_add_contact_default_parameters(self):
        print("=== test_create_add_contact_default_parameters ===")
        self.assertTrue(issubclass(AddContact, View))
        self.assertTrue(isinstance(self.view_add_contact, View))
        self.assertTrue(isinstance(self.view_add_contact, AddContact))
        self.assertEqual(self.view_add_contact.title, "Add Contact")
        self.assertEqual(self.view_add_contact.size, (420, 400))
        # Ensure the names match with their widget
        for i, name in enumerate(self.component_names):
            self.assertIsInstance(
                    self.view_add_contact.get_component(name),
                    self.widgets[i])

    def test_submit(self):
        print("=== test_submit ===")
        name_entry_text = "contact_name"
        email_entry_text = "contact@email.com"
        name_entry = self.view_add_contact.get_component("txt_contact_name")
        email_entry = self.view_add_contact.get_component("txt_contact_email")
        name_entry.insert(0, name_entry_text)
        email_entry.insert(0, email_entry_text)
        details = self.view_add_contact.submit()
        self.assertEqual(name_entry.get(), name_entry_text)
        self.assertEqual(email_entry.get(), email_entry_text)
        self.assertEqual(details, [name_entry_text, email_entry_text])

    def test_clear(self):
        print("=== test_clear ===")
        name_entry_text = "contact_name"
        email_entry_text = "contact@email.com"
        name_entry = self.view_add_contact.get_component("txt_contact_name")
        email_entry = self.view_add_contact.get_component("txt_contact_email")
        name_entry.insert(0, name_entry_text)
        email_entry.insert(0, email_entry_text)

        self.assertEqual(name_entry.get(), name_entry_text)
        self.assertEqual(email_entry.get(), email_entry_text)

        self.view_add_contact.clear()

        self.assertEqual(name_entry.get(), '')
        self.assertEqual(email_entry.get(), '')

    def tearDown(self):
        self.view_add_contact.tk.destroy()
        self.view_add_contact = None


if __name__ == '__main__':
    unittest.main()
