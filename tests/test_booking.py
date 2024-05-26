# tests/test_booking.py
from src.booking.booking import Booking
from datetime import datetime
import unittest


class TestBooking(unittest.TestCase):

    def setUp(self):
        self.booking = Booking()
        self.invalid_string_values = [
                85, 1.0, datetime.now(), [], [1, 2, 3], {"title": "my_title"}]
        self.invalid_datetime_values = [
                88, 2.2, [], [1, 2, 3], (), {"date": 2024}, "2024, 12, 27"]
        self.invalid_int_tuple_values = [
                92, 2.1, [], [1, 2, 3], {"time": "3:30"}, "20:12"]

    def tearDown(self):
        self.booking = None

    def test_create_booking_successful(self):
        print("=== test_create_booking_successful ===")
        # Arrange
        title = "Dr Appointment"
        date = (2024, 5, 15)
        time = (14, 30)
        contact = "Dr Smith"
        description = "Annual check-up"

        # Act
        booking = Booking(_title=title,
                          _date=date,
                          _time=time,
                          _contact=contact,
                          _description=description
                          )
        # Assert
        self.assertEqual(booking.title, title)
        self.assertEqual(booking.date, date)
        self.assertEqual(booking.time, time)
        self.assertEqual(booking.contact, contact)
        self.assertEqual(booking.description, description)
        expected_repr_str = str(
                "Booking(title='Dr Appointment', " +
                "date=(2024, 5, 15), " +
                "time=(14, 30), " +
                "contact='Dr Smith', " +
                "description='Annual check-up')")
        self.assertEqual(booking.__repr__(), expected_repr_str)

    def test_create_booking_with_default_parameters(self):
        print("=== test_create_booking_with_default_parameters_successful ===")
        dt = datetime.now()
        self.assertEqual(self.booking.title, "New Booking")
        self.assertEqual(self.booking.date, (dt.year, dt.month, dt.day))
        self.assertEqual(self.booking.time, (dt.hour, dt.minute))
        self.assertEqual(self.booking.contact, "New Contact")
        self.assertEqual(self.booking.description, "Enter a description.")
        expected_repr_str = str(
                "Booking(title='New Booking', " +
                f"date=({dt.year}, {dt.month}, {dt.day}), " +
                f"time=({dt.hour}, {dt.minute}), " +
                "contact='New Contact', " +
                "description='Enter a description.')")

        self.assertEqual(self.booking.__repr__(), expected_repr_str)

    def test_set_title_property_successful(self):
        print("=== test_set_title_property_successful ===")

        self.booking.title = "Phone Appointment"
        self.assertIsInstance(self.booking.title, str)
        self.assertEqual(self.booking.title, "Phone Appointment")

    def test_set_title_property_failure(self):
        print("=== test_set_title_property_failure ===")

        for invalid_value in self.invalid_string_values:
            with self.subTest(
                msg="Test setting 'title' property to invalid string values",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.booking.title = invalid_value

        value_error_input = ["", ' ', None]
        for invalid_value in value_error_input:
            with self.subTest(value=invalid_value):
                with self.assertRaises(ValueError):
                    self.booking.title = invalid_value

    def test_set_date_property_successful(self):
        print("=== test_set_date_property_successful ===")
        dt = datetime.now()
        self.booking.date = dt
        self.assertIsInstance(self.booking.date, datetime)
        self.assertEqual(self.booking.date, dt)

    def test_set_date_property_failure(self):
        print("=== test_set_date_property_failure ===")

        with self.subTest(
                msg="Test setting 'date' property to invalid datetime values"):
            for value in self.invalid_datetime_values:
                with self.assertRaises(TypeError):
                    self.booking.date = value

        with self.subTest(msg="Test setting 'date' property to None"):
            with self.assertRaises(ValueError):
                self.booking.date = None

    def test_set_time_property_successful(self):
        print("=== test_set_time_property_successful ===")
        dt = datetime.now()
        self.booking.time = (dt.hour, dt.minute)
        self.assertIsInstance(self.booking.time, tuple)
        self.assertEqual(self.booking.time, (dt.hour, dt.minute))

    def test_set_time_property_failure(self):
        print("=== test_set_time_property_failure ===")

        with self.subTest(
                msg="Test setting 'time' property to invalid time values"):
            for value in self.invalid_int_tuple_values:
                with self.assertRaises(TypeError):
                    self.booking.time = value

        value_error_input = [None, (), (-1, 30), (24, 20), (12, -1), (23, 60)]
        for invalid_value in value_error_input:
            with self.subTest(
                msg="Test setting 'time' property to None, an empty tuple, " +
                "beyond the limits of 24 hour time format.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    self.booking.time = invalid_value

    def test_set_contact_property_successful(self):
        print("=== test_set_contact_property_successful ===")

        self.booking.contact = "Test Contact"
        self.assertIsInstance(self.booking.contact, str)
        self.assertEqual(self.booking.contact, "Test Contact")

    def test_set_contact_property_failure(self):
        print("=== test_set_contact_property_failure ===")

        for invalid_value in self.invalid_string_values:
            with self.subTest(
                msg="Test setting 'contact' property to invalid string" +
                    " values.", value=invalid_value):
                with self.assertRaises(TypeError):
                    self.booking.contact = invalid_value

        value_error_input = [None, "", ' ']
        for invalid_value in value_error_input:
            with self.subTest(msg="Test setting 'contact property to None, " +
                              "white space and an empty string.'",
                              value=invalid_value):
                with self.assertRaises(ValueError):
                    self.booking.contact = invalid_value

    def test_set_description_property_successful(self):
        print("=== test_set_description_property_successful ===")

        self.booking.description = "Test description"
        self.assertIsInstance(self.booking.description, str)
        self.assertEqual(self.booking.description, "Test description")

    def test_set_description_property_failure(self):
        print("=== test_set_description_property_failure ===")

        for invalid_value in self.invalid_string_values:
            with self.subTest(
                    msg="Test setting 'description' to invalid string values.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    self.booking.description = invalid_value

        value_error_input = [None, "", ' ']
        for invalid_value in value_error_input:
            with self.subTest(
                    msg="Test setting 'description' to None, white space and" +
                    "an empty string.", value=invalid_value):
                with self.assertRaises(ValueError):
                    self.booking.description = invalid_value

    def test___repr__with_default_values(self):
        dt = datetime.now()
        expected_repr_str = str(
            "Booking(title='New Booking', " +
            f"date=({dt.year}, {dt.month}, {dt.day}), " +
            f"time=({dt.hour}, {dt.minute}), " +
            "contact='New Contact', " +
            "description='Enter a description.')")
        self.assertEqual(self.booking.__repr__(), expected_repr_str)


if __name__ == '__main__':
    unittest.main()
