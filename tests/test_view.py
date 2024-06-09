# tests/test_view.py
import unittest
from src.views.view import View
import tkinter as tk
from tkinter import ttk as ttk
import datetime
from tkcalendar import DateEntry


class TestView(unittest.TestCase):

    def setUp(self):
        self.view = View()

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
        self.assertIsInstance(button, tk.Button)
        self.assertEqual(button.name, "button")
        self.assertEqual(button.cget('text'), "Click me")
        self.assertEqual(button.command, None)
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
        self.assertIsInstance(self.view.get_component("my_button"), tk.Button)
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
        self.assertEqual(entry_text.show, None)
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

    def test_create_dropdown_successful(self):
        print("=== test_create_dropdown_successful ===")
        dropdown = self.view.create_dropdown()
        self.assertIsNotNone(dropdown)
        self.assertIsInstance(dropdown, ttk.Combobox)
        self.assertIsInstance(dropdown.name, str)
        self.assertIsInstance(dropdown.x, int)
        self.assertIsInstance(dropdown.y, int)
        self.assertIsInstance(dropdown.values, list)
        self.assertIsInstance(dropdown.width, int)
        self.assertIsInstance(dropdown.textvariable, tk.StringVar)
        self.assertEqual(dropdown.name, "dropdown")
        self.assertEqual(dropdown.x, 0)
        self.assertEqual(dropdown.y, 0)
        self.assertEqual(dropdown.values, ["Option 1", "Option 2", "Option 3"])
        self.assertEqual(dropdown.width, 20)
        self.assertEqual(dropdown.textvariable.get(), "")

    def test_create_dropdown_failure_name_parameter(self):
        print("=== test_create_dropdown_failure_name_parameter ===")
        # name - ValueError
        raises_value_errors = [None, "", " "]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values that raise a ValueError exception " +
                "with the 'name' parameter.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.create_dropdown(name=invalid_value)
        # name - TypeError
        raises_type_errors = [1, 2.1, (), [], {}, tk, tk.StringVar]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception " +
                "with the 'name' parameter.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.create_dropdown(name=invalid_value)

    def test_create_dropdown_failure_values_parameter(self):
        print("=== test_create_dropdown_failure_values_parameter ===")
        # values - ValueError
        raises_value_errors = [None, "", " "]
        with self.assertRaises(ValueError):
            self.view.create_dropdown(values=raises_value_errors)
        # values - TypeError
        raises_type_errors = [1, 2.1, (), [], {}, tk, tk.StringVar]
        with self.assertRaises(TypeError):
            self.view.create_dropdown(values=raises_type_errors)

    def test_create_dropdown_failure_int_parameters(self):
        print("=== test_create_dropdown_failure_int_parameters ===")
        # x, y, width ValueError
        raises_value_errors = [None, -1]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values that raise a ValueError exception " +
                "with the 'x', 'y', and 'width' parameters.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.create_dropdown(x=invalid_value)
                    self.view.create_dropdown(y=invalid_value)
                    self.view.create_dropdown(width=invalid_value)
        # x, y, with TypeError
        raises_type_errors = [
                2.2, " ", {}, [], (), tk, tk.IntVar, tk.StringVar]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception " +
                "with 'x', 'y', and 'width' parameters.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.create_dropdown(x=invalid_value)
                    self.view.create_dropdown(y=invalid_value)
                    self.view.create_dropdown(width=invalid_value)

    # create_spinbox
    def test_create_spinbox(self):
        print("=== test_create_spinbox ===")
        spinbox = self.view.create_spinbox()
        self.assertIsNotNone(spinbox)
        self.assertIsInstance(spinbox, tk.Spinbox)
        self.assertIsInstance(spinbox.name, str)
        self.assertIsInstance(spinbox.x, int)
        self.assertIsInstance(spinbox.y, int)
        self.assertIsInstance(spinbox.from_, int)
        self.assertIsInstance(spinbox.to, int)
        self.assertIsInstance(spinbox.increment, int)
        self.assertIsInstance(spinbox.width, int)
        self.assertIsInstance(spinbox.textvariable, tk.StringVar)
        self.assertIsInstance(spinbox.numvar, tk.IntVar)
        self.assertEqual(spinbox.name, "spinbox")
        self.assertEqual(spinbox.x, 0)
        self.assertEqual(spinbox.y, 0)
        self.assertEqual(spinbox.from_, 0)
        self.assertEqual(spinbox.to, 100)
        self.assertEqual(spinbox.increment, 1)
        self.assertEqual(spinbox.width, 20)
        self.assertEqual(spinbox.textvariable.get(), "0")
        self.assertEqual(spinbox.numvar.get(), 0)

    def test_create_spinbox_failure_name_parameter(self):
        print("=== test_create_spinbox_failure_name_parameter ===")
        # name - ValueError
        raises_value_errors = [None, "",  " "]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values that rasie a ValueError exception " +
                "with the 'name' parameter.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.create_spinbox(name=invalid_value)
        # name - TypeError
        raises_type_errors = [2, 1.2, (), [], {}, tk, tk.StringVar, tk.IntVar]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception " +
                "with the 'name' parameter.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.create_spinbox(name=invalid_value)

    def test_create_spinbox_failure_value_errors_int_parameters(self):
        t_name = str("test_create_spinbox_failure_value_errors_int_parameters")
        print(f"=== {t_name} ===")
        # x, y, from_, to, increment, width - ValueError
        raises_value_errors = [None, -1]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values the raise a ValueError " +
                "with the 'x', 'y', 'from_', 'to', 'increment', " +
                "and 'width' parameters.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.create_spinbox(x=invalid_value)
                    self.view.create_spinbox(y=invalid_value)
                    self.view.create_spinbox(from_=invalid_value)
                    self.view.create_spinbox(to=invalid_value)
                    self.view.create_spinbox(increment=invalid_value)
                    self.view.create_spinbox(width=invalid_value)

    def test_create_spinbox_failure_type_errors_int_parameters(self):
        t_name = str("test_create_spinbox_failure_type_errors_int_parameters")
        print(f"=== {t_name} ===")
        # x, y, from_, to, increment, width - TypeError
        raises_type_errors = [
            "test", " ", "", 2.1, (), (1,), (1, 2, 3), {}, [], [1,], [1, 2,],
            tk, tk.StringVar, tk.IntVar]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values the raise a TypeError " +
                "with the 'x', 'y', 'from_', 'to', 'increment', " +
                "and 'width' parameters.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.create_spinbox(x=invalid_value)
                    self.view.create_spinbox(y=invalid_value)
                    self.view.create_spinbox(from_=invalid_value)
                    self.view.create_spinbox(to=invalid_value)
                    self.view.create_spinbox(increment=invalid_value)
                    self.view.create_spinbox(width=invalid_value)

    # create_calendar
    def test_create_calendar_successful(self):
        print("=== test_create_calendar_successful ===")
        calendar = self.view.create_calender()
        self.assertIsNotNone(calendar)
        self.assertIsInstance(calendar, DateEntry)
        self.assertIsInstance(calendar.name, str)
        self.assertIsInstance(calendar.x, int)
        self.assertIsInstance(calendar.y, int)
        self.assertIsInstance(calendar.width, int)
        self.assertEqual(calendar.name, "calendar")
        self.assertEqual(calendar.x, 0)
        self.assertEqual(calendar.y, 0)
        self.assertEqual(calendar.width, 20)
        date_today = datetime.datetime.today()
        year = date_today.year
        month = date_today.month
        day = date_today.day
        self.assertEqual(calendar.get_date(), datetime.date(year, month, day))
        calendar.set_date("5/6/24")
        # should return a datetime.date(2024, 6, 5)
        self.assertEqual(calendar.get_date(), datetime.date(2024, 6, 5))
        calendar.destroy()

    def test_create_calendar_failure_name_parameter(self):
        print("=== test_create_calendar_failure_name_parameter ===")
        # name - ValueError
        raises_value_errors = [None, "", " "]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values that raise a ValueError exception " +
                "with the 'name' parameter.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.create_calender(name=invalid_value)
        # name - TypeError
        raises_type_errors = [1, 2.1, [], (), {}, tk, tk.StringVar, tk.IntVar]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception " +
                "with the 'name' parameter.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.create_calender(name=invalid_value)

    def test_create_calendar_failure_value_error_x_y_width_parameters(self):
        t_name = str("test_create_calendar_failure_value_error" +
                     "_x_y_width_parameters")
        print(f"=== {t_name} ===")
        # x, y, width - ValueError
        raises_value_errors = [None, -1]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values that raise a ValueError exception " +
                "with the 'x', 'y', and 'width' parameters.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.create_calender(x=invalid_value)
                    self.view.create_calender(y=invalid_value)
                    self.view.create_calender(width=invalid_value)

    def test_create_calendar_failure_type_error_x_y_width_parameters(self):
        t_name = str("test_create_calendar_failure_type_error" +
                     "_x_y_width_parameters")
        print(f"=== {t_name} ===")
        # x, y, width - TypeError
        raises_type_errors = [
            "test", " ", "", 2.1, (), (1,), (1, 2, 3), {}, [], [1,], [1, 2,],
            tk, tk.StringVar, tk.IntVar]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception " +
                "with the 'x', 'y', and 'width' parameters.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.create_calender(x=invalid_value)
                    self.view.create_calender(y=invalid_value)
                    self.view.create_calender(width=invalid_value)

    def test_set_font_successful(self):
        print("=== test_set_font_successful ==")
        # create a label to test with
        lbl_test = self.view.create_label(
                name="lbl_test", text="test_font", x=10, y=10)

        self.assertIsInstance(lbl_test, ttk.Label)
        self.assertIsInstance(lbl_test.font, list)
        # Testing the default values
        self.assertIn({'family': "Arial"}, lbl_test.font)
        self.assertIn({'size': 9}, lbl_test.font)
        self.assertIn({'weight': "normal"}, lbl_test.font)
        self.assertIn({'slant': "roman"}, lbl_test.font)
        self.assertIn({'underline': 0}, lbl_test.font)

        # Testing with manual values, ommiting the font_style tuple
        self.view.set_font(
                component_name=lbl_test.name,
                font_family="Arial",
                font_size=14
                )
        self.assertIn({'family': "Arial"}, lbl_test.font)
        self.assertIn({'size': 14}, lbl_test.font)
        self.assertIn({'weight': "normal"}, lbl_test.font)
        self.assertIn({'slant': "roman"}, lbl_test.font)
        self.assertIn({'underline': 0}, lbl_test.font)

        # Testing with manual values with a complete font_style tuple
        self.view.set_font(
                component_name=lbl_test.name,
                font_family="Verdana",
                font_size=16,
                font_style=("bold", "roman", "no_underline"))
        self.assertIn({'family': "Verdana"}, lbl_test.font)
        self.assertIn({'size': 16}, lbl_test.font)
        self.assertIn({'weight': "bold"}, lbl_test.font)
        self.assertIn({'slant': "roman"}, lbl_test.font)
        self.assertIn({'underline': 0}, lbl_test.font)

        # Testing with manual values with an incomplete font_style tuple
        '''NOTE: font_style values must be in order.
            weight, slant, underline.
            Failure to follow this will result in a ValueError.
            e.g. 'bold', 'underline' will fail,
            'italic', 'bold' will fail,
            'underline', 'bold', 'italic' will also fail.
            '''
        self.view.set_font(
                component_name=lbl_test.name,
                font_family="Helvetica",
                font_size=16,
                font_style=("bold", 'roman'))
        self.assertIn({'family': "Helvetica"}, lbl_test.font)
        self.assertIn({'size': 16}, lbl_test.font)
        self.assertIn({'weight': "bold"}, lbl_test.font)
        self.assertIn({'slant': "roman"}, lbl_test.font)
        self.assertIn({'underline': 0}, lbl_test.font)

    def test_set_font_failure(self):
        print("=== test_set_font_failure ===")
        # Successful implementation
        self.view.create_label("lbl_test", x=0, y=0)
        lbl_test = self.view.set_font(
                "lbl_test", "Verdana", 14, (
                    "normal", "italic", "no_underline"))
        self.assertIn({'family': "Verdana"}, lbl_test.font)
        self.assertIn({'size': 14}, lbl_test.font)
        self.assertIn({'weight': "normal"}, lbl_test.font)
        self.assertIn({'slant': "italic"}, lbl_test.font)
        self.assertIn({'underline': 0}, lbl_test.font)

        # Failure
        # name, font_family, font_style - ValueErrors
        raises_str_value_errors = [None, "", " "]
        for invalid_value in raises_str_value_errors:
            with self.subTest(
                msg="Test values that raise a ValueError exception for the " +
                "'name', 'font_family', 'font_style' parameters.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.set_font(invalid_value, "Verdana", 14, (
                        "normal", "italic", "no_underline"))
                    self.view.set_font("lbl_test", invalid_value, 14, (
                        "normal", "italic", "no_underline"))
                    self.view.set_font("lbl_test", "Verdana", 14, (
                        invalid_value, "italic", "no_underline"))
                    self.view.set_font("lbl_test", "Verdana", 14, (
                        "normal", invalid_value, "no_underline"))
                    self.view.set_font("lbl_test", "Verdana", 14, (
                        "normal", "italic", invalid_value))

        # name, font_family, font_style - TypeErrors
        raises_str_type_errors = [1, 2.3, [], (), {}, self.view]
        for invalid_value in raises_str_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception for the" +
                "'name', 'font_family', 'font_style' parameters.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.set_font(invalid_value, "Verdana", 14, (
                        "normal", "italic", "no_underline"))
                    self.view.set_font("lbl_test", invalid_value, 14, (
                        "normal", "italic", "no_underline"))
                    self.view.set_font("lbl_test", "Verdana", 14, (
                        invalid_value, "italic", "no_underline"))
                    self.view.set_font("lbl_test", "Verdana", 14, (
                        "normal", invalid_value, "no_underline"))
                    self.view.set_font("lbl_test", "Verdana", 14, (
                        "normal", "italic", invalid_value))

        # font_size - ValueErrors
        raises_int_value_errors = [None, -1]
        for invalid_value in raises_int_value_errors:
            with self.subTest(
                msg="Test values that raise a ValueError exception for the" +
                "'font_size' parameter.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.view.set_font("lbl_test", "Verdana", invalid_value, (
                        "normal", "italic", "no_underline"))

        # font_size - TypeErrors
        raises_int_type_errors = [2.1, [], " ", (), {}, self.view]
        for invalid_value in raises_int_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception for the" +
                "'font_size' parameter.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.view.set_font("lbl_test", "Verdana", invalid_value, (
                        "normal", "italic", "no_underline"))

    def tearDown(self):
        for comp in self.view.components:
            if isinstance(comp, DateEntry):
                comp.destroy()
        self.view.components.clear()
        self.view.components = None
        self.view.tk.destroy()
        self.view = None


if __name__ == '__main__':
    unittest.main()
