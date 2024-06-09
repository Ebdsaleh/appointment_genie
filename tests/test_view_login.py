# tests/test_view_login.py
import unittest
from src.views.login import Login
from src.views.view import View
import tkinter as tk
import tkinter.ttk as ttk


class TestViewLogin(unittest.TestCase):
    def setUp(self):
        print("=== setUp Login()")
        self.login = Login()
        self.default_component_keys = [
                'main_frame', 'lbl_login', 'lbl_username', 'lbl_password',
                'txt_username', 'txt_password', 'btn_submit']
        self.default_component_instances = [
                ttk.Frame, ttk.Label, ttk.Label, ttk.Label, tk.Entry, tk.Entry,
                tk.Button]

    def test_create_login_default_parameters(self):
        print("=== test_create_login ===")
        self.assertIsInstance(self.login, Login)
        self.assertTrue(issubclass(Login, View))
        self.assertIsInstance(self.login.title, str)
        self.assertIsInstance(self.login.size, tuple)
        self.assertIsInstance(self.login.size[0], int)
        self.assertIsInstance(self.login.size[1], int)
        self.assertIsInstance(self.login.components, list)
        self.assertEqual(self.login.title, "Login")
        self.assertEqual(self.login.size, (300, 400))

    def test_setup_ui(self):
        print("=== test_setup_ui ===")
        # setup_ui is called during the __init__() method of the class.
        # So no need to invoke it explicitly here.

        for i, comp_key in enumerate(self.default_component_keys):
            component = self.login.get_component(comp_key)
            self.assertIsInstance(
                    component, self.default_component_instances[i])

    def test_submit(self):
        print("=== test_submit ===")
        password_entry = self.login.get_component('txt_password')
        submit_button = self.login.get_component('btn_submit')
        test_password = "testpassword"
        password_entry.insert(0, test_password)
        submit_button.invoke()
        self.assertEqual(self.login.submit(), test_password)

    def tearDown(self):
        self.login.tk.destroy()
        self.login = None
        self.defaulf_component_keys = None
        self.default_component_instances = None


if __name__ == '__main__':
    unittest.main()
