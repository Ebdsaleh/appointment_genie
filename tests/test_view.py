# tests/test_view.py
import unittest
from src.views.view import View
import tkinter as tk
from tkinter import ttk


class TestView(unittest.TestCase):

    def setUp(self):
        self.view = View()

    def tearDown(self):
        self.view = None

    def test_create_view_with_default_values(self):
        print("=== test_create_view ===")
        self.assertIsInstance(self.view, View)
        self.assertIsInstance(self.view.title, str)
        self.assertIsInstance(self.view.size, tuple)
        self.assertIsInstance(self.view.width, int)
        self.assertIsInstance(self.view.height, int)
        self.assertIsInstance(self.view.components, list)
        self.assertIsInstance(self.view.tk, tk.Tk)
        self.assertIsInstance(self.view.frame, ttk.Frame)
        self.assertEqual(self.view.title, "new_view")
        self.assertEqual(self.view.size, (300, 400))
        self.assertEqual(self.view.width, 300)
        self.assertEqual(self.view.height, 400)
        self.assertEqual(len(self.view.components), 1)
        self.assertTrue(hasattr(self.view, 'tk'))
        self.assertTrue(hasattr(self.view.tk, 'geometry'))
        self.assertTrue(hasattr(self.view.tk, 'title'))

    def test_create_view_with_non_default_values(self):
        print("=== test_create_view_with_non_default_values ===")
        v = View("Test View", (800, 600))
        self.assertIsInstance(v, View)
        self.assertEqual(v.title, "Test View")
        self.assertEqual(v.size, (800, 600))
        self.assertEqual(v.width, 800)
        self.assertEqual(v.height, 600)
        self.assertEqual(len(v.components), 1)
        self.assertTrue(hasattr(v, 'tk'))
        self.assertTrue(hasattr(v.tk, 'title'))
        self.assertTrue(hasattr(v.tk, 'geometry'))

    def test_set_title_property(self):
        self.view.title = "My new view"
        self.assertEqual(self.view.title, "My new view")
        # ValueErrors
        raises_value_errors = ["", None, " "]
        for invalid_value in raises_value_errors:
            with self.subTest(
                    msg="Test values that raise a ValueError exception " +
                    "when setting the 'title' property.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.title = invalid_value
        # TypeErrors
        raises_type_errors = [12, 2.1, [], (), {}, tk]
        for invalid_value in raises_type_errors:
            with self.subTest(
                    msg="Test values that raise a TypeError exception " +
                    "when setting the 'title' property.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.title = invalid_value

    def test_set_size_property(self):
        print("=== test_set_size_property ===")
        self.view.size = (800, 600)
        self.assertEqual(self.view.size, (800, 600))
        # ValueErrors
        raises_value_errors = [None, (), (1, 2, 3)]
        for invalid_value in raises_value_errors:
            with self.subTest(
                    msg="Test values that raise a ValueError exception " +
                    "when setting the 'size' property.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.size = invalid_value
        # TypeErrors
        raises_type_errors = [(1), 2.1, (2.3, 3.3), [], {}, tk, "", "size"]
        for invalid_value in raises_type_errors:
            with self.subTest(
                    msg="Test values that raise a TypeError exception " +
                    "when setting the 'size' property.",
                        value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.size = invalid_value

    def test_set_width_property(self):
        print("=== test_width_property ===")
        self.view.width = 800
        self.assertIsInstance(self.view.width, int)
        self.assertEqual(self.view.width, 800)
        # Test that the size value updates accordingly when width is changed
        self.assertEqual(self.view.size, (800, 400))
        # ValueErrors
        raises_value_errors = None
        with self.assertRaises(ValueError):
            self.view.width = raises_value_errors
        # TypeErrors
        raises_type_errors = [
                (), (1, 2, 3), [], {}, "", " ", tk, self.view.size]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception " +
                "when setting the 'width' property.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.width = invalid_value

    def test_set_height_property(self):
        print("=== test_set_height_property ===")
        self.view.height = 600
        self.assertIsInstance(self.view.height, int)
        self.assertEqual(self.view.height, 600)
        # Test that the size value updates accordingly when height is changed.
        self.assertEqual(self.view.size, (self.view.width, self.view.height))
        # ValueErrors
        raises_value_errors = None
        with self.assertRaises(ValueError):
            self.view.height = raises_value_errors
        # TypeErrors
        raises_type_errors = [
                (1, 3, 4), [], {}, self.view.size, "", " ", tk, ()]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception when " +
                "setting the 'height' property.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.height = invalid_value

    def test_create_button(self):
        button = self.view.create_button()
        self.assertIsInstance(button, ttk.Button)
        self.assertEqual(button.name, "button")
        self.assertEqual(button.cget('text'), "Click me")
        self.assertEqual(button.place_info().get('x', 0), str(0))
        self.assertEqual(button.place_info().get('y', 0), str(0))
        self.assertEqual(
                self.view.components,
                [{self.view.frame.name: self.view.frame}, {"button": button}])
        self.assertIn({button.name: button}, self.view.components)

    def test_get_component(self):
        print("=== test_get_component ===")
        self.view.create_button("my_button", text="Click me", x=10, y=0)
        button = self.view.get_component("my_button")
        self.assertEqual(button.cget("text"), "Click me")
        self.assertEqual(button.place_info().get('x', 10), str(10))
        self.assertEqual(button.place_info().get('y', 0), str(0))
        self.assertIsInstance(self.view.get_component("my_button"), ttk.Button)
        self.assertTrue(len(self.view.components), 2)

        # Check for non exisitent values
        submit_button = self.view.get_component("submit_button")
        self.assertIsNone(self.view.get_component("submit_button"))
        self.assertIsNone(submit_button)
        # ValueErrors
        raises_value_errors = [None, "", " "]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values that raise a ValueError exception " +
                "when using 'get_component'.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.get_component(invalid_value)

        # TypeErrors
        raises_type_errors = [1, 2.1, {}, [], (), tk]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception " +
                "when using'get_component'.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.get_component(invalid_value)

    def test_create_label(self):
        print("=== test_create_label ===")
        self.view.create_label("my_label", "test_label")
        label = self.view.get_component("my_label")
        self.assertIsInstance(label, ttk.Label)
        self.assertEqual(label.cget('text'), "test_label")
        self.assertTrue(len(self.view.components), 2)

        # ValueErrors
        raises_value_errors = [None, "", " "]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values that raise a ValueError exception " +
                "when creating a 'label'.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.create_label(invalid_value, "test_label")
                    self.view.create_label("my_label", invalid_value)

        # TypeErrors
        raises_type_errors = [1, 2.1, {}, [], (), tk]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception " +
                "when creating a 'label'.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.create_label(invalid_value, "test_label")
                    self.view.create_label("my_label", invalid_value)

    def test_create_entry_text_field(self):
        print("=== test_create_entry_text_field ===")
        entry_text = self.view.create_entry_text_field("test_entry")
        self.assertIsInstance(entry_text, tk.Entry)
        self.assertIsNotNone(entry_text)
        self.assertEqual(entry_text.name, 'test_entry')
        self.assertEqual(len(self.view.components), 2)

        # name - ValueErrors
        raises_value_errors = [None, "", " "]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values that raise a ValueError exception " +
                "for the 'name' parameter.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.create_entry_text_field(invalid_value)
        # width - ValueErrors
        for number in range(-10, 11):
            with self.subTest(
                msg="Test values that raise a ValueError exception " +
                "with the 'width' property",
                    value=number):
                with self.assertRaises(ValueError):
                    self.view.create_entry_text_field('test_entry', number)

        # name - TypeErrors
        raises_type_errors = [1, 2.3, (), [], {}, tk]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception " +
                "with the 'name' parameter.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.create_entry_text_field(invalid_value)
        # width - TypeError
        raises_type_errors = [2.3, (), [1, 2, 3], {}, tk]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception " +
                "with the 'width' parameter.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.create_entry_text_field(
                            "test_entry", invalid_value)


if __name__ == '__main__':
    unittest.main()
