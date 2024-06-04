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

    def tearDown(self):
        self.login.tk.destroy()
        self.login = None
        self.defaulf_component_keys = None
        self.default_component_instances = None

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
        default_key_iter = iter(self.default_component_keys)
        default_inst_iter = iter(self.default_component_instances)
        login_components_iter = iter(self.login.components)

        for i in range(0, len(self.login.components)):
            comp_key = next(default_key_iter)
            login_comp_keys = next(login_components_iter).keys()
            comp_inst = next(default_inst_iter)
            self.assertIn(comp_key, login_comp_keys)
            self.assertIsInstance(
                    self.login.components[i][self.default_component_keys[i]],
                    comp_inst)


if __name__ == '__main__':
    unittest.main()
