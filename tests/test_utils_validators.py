# tests/test_utils_validators.py
import src.utils.validators as val
from datetime import datetime
import unittest


class TestUtilsValidators(unittest.TestCase):
    """
    This Class will test the functions in the src/utils/validators.py file.
    These functions are used to validate arugments passed into functions,
    class properties.
    """

    def setUp(self):
        self.dt = datetime.now()
        self.invalid_datetime_values = [
                "2024, 5, 26", None, (2024, 5, 26), 1237450947, 12, 13.50,
                {"datetime": 2005}, True, False]
        # Can work with generic boolean assertions
        self.invalid_int_values = [0.1, " ", "", "hello", [], {}, (), None]
        self.invalid_tuple_values = [0, 1.2, " ", "hello?", [], {}, None]
        self.invalid_string_values = [1, 2.2, [2, 3], {}, (), self.dt, None]
        self.invalid_generic_string_type_error_values = [
                1, 2.2, [2, 3], {}, ()]

    def tearDown(self):
        self.dt = None
        self.invalid_datetime_values = None
        self.invalid_int_values = None
        self.invalid_tuple_values = None
        self.invalid_string_values = None

    # Generic validation of types
    def test_is_valid_string(self):
        print("=== test_is_valid_string ===")
        self.assertTrue(val.is_valid_string("hello"))
        self.assertFalse(val.is_valid_string(100))

    def test_is_valid_datetime(self):
        print("=== test_is_valid_datetime ===")
        self.assertTrue(val.is_valid_datetime(self.dt))
        for invalid_value in self.invalid_datetime_values:
            with self.subTest(
                    msg="Test invalid datetime values with " +
                    "'is_valid_datetime'.", value=invalid_value):
                self.assertFalse(val.is_valid_datetime(invalid_value))

    def test_is_valid_int(self):
        print("=== test_is_valid_int ===")
        self.assertTrue(val.is_valid_int(10))
        for invalid_value in self.invalid_int_values:
            with self.subTest(
                    msg="Test invalid int values. with 'is_valid_int'.",
                    value=invalid_value):
                self.assertFalse(val.is_valid_int(invalid_value))

    def test_is_valid_tuple(self):
        print("=== test_is_valid_tuple ===")
        self.assertTrue(val.is_valid_tuple((1, 2, 3)))
        for invalid_value in self.invalid_tuple_values:
            with self.subTest(
                    msg="Test invalid tuple values with 'is_valid_tuple'",
                    value=invalid_value):
                self.assertFalse(val.is_valid_tuple(invalid_value))

    def test_is_valid_dict(self):
        print("=== test_is_valid_dict ===")
        self.assertTrue(val.is_valid_dict({}))
        self.assertTrue(val.is_valid_dict({"dict": "is_dict"}))
        self.assertFalse(val.is_valid_dict("not a dict!"))

    # Property tests
    def test_validate_string_property_successful(self):
        print("=== test_validate_string_property ===")
        value = "test_string"
        property_name = "test_property"

        # Expect to return None if OK
        self.assertEqual(val.validate_string_property(value, property_name),
                         None)

    def test_validate_string_property_failure(self):
        print("=== test_validate_string_property_failure ===")

        # value parameter - string
        will_raise_type_errors = [1, 2.0, (1, 2, 3), (), {},
                                  {"value": 'value'}, self.dt, True, False]
        for invalid_value in will_raise_type_errors:
            with self.subTest(
                    msg="Test values that will raise a TypeError exception " +
                    "with 'validate_string_property' for the 'value' " +
                    "parameter",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    val.validate_string_property(invalid_value,
                                                 "test_property")
        # property_name parameter - string
        will_raise_value_errors = [None, "", " "]
        for invalid_value in will_raise_value_errors:
            with self.subTest(
                    msg="Test values that will raise a ValueError exception " +
                    "with 'validate_string_property' for the " +
                    "'value' and 'property_name' parameters",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    val.validate_string_property(invalid_value,
                                                 "test_property")
                    val.validate_string_property("testing", invalid_value)

    def test_validate_datetime_property_successful(self):
        print("=== test_validate_datetime_property_successful ===")
        value = self.dt
        property_name = "datetime test"

        # Expect None if OK
        self.assertEqual(
                val.validate_datetime_property(value, property_name), None)

    def test_validate_datetime_property_failure(self):
        print("=== test_validate_datetime_property_failure ===")

        # value parameter - datetime object
        will_raise_type_errors = [1, 2.3, " ", "", {"datetime": self.dt},
                                  (), {}, (2004, 10, 1), [], [1, 2, 3],
                                  True, False]
        for invalid_value in will_raise_type_errors:
            with self.subTest(
                    msg="Test values that will raise a TypeError exception " +
                    "with 'validate_datetime_property', for the " +
                    "'value' parameter",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    val.validate_datetime_property(invalid_value, "datetime")

        # No need to check datetime values that's handled in the datetime class

        # property_name - string
        will_raise_type_errors_for_property_name = [1, 2.2, [2, 3], {}, (),
                                                    self.dt]
        for invalid_value in will_raise_type_errors_for_property_name:
            with self.subTest(
                    msg="Test values that will raise a TypeError exception " +
                    "with 'validate_datetime_property' for the " +
                    "'property_name' parameter.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    val.validate_datetime_property(self.dt, invalid_value)

        will_raise_value_errors = [None, "", " "]
        for invalid_value in will_raise_value_errors:
            with self.subTest(
                    msg="Test values that will raise a ValueError exception " +
                    "with 'validate_datetime_property', for the " +
                    "'property_name' parameter",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    val.validate_datetime_property(self.dt, invalid_value)

    def test_validate_int_tuple_property_successful(self):
        print("=== test_validate_int_tuple_property_successful ===")
        value = (1, 2, 3)
        property_name = "int_tuple_test"

        # Expect None if OK
        self.assertEqual(
                val.validate_int_tuple_property(value, property_name), None)

    def test_validate_int_tuple_property_failure(self):
        print("=== test_validate_int_tuple_property_failure ===")
        will_raise_type_errors = [" ", 1, 2.5, [], [1, 2, 3],
                                  {"tuple": 123}, True, False]
        # value paramter - tuple of ints
        for invalid_value in will_raise_type_errors:
            with self.subTest(
                    msg="Test values that will raise a TypeError exception " +
                    "with 'validate_int_tuple_property' for the 'value' " +
                    "parameter.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    val.validate_int_tuple_property(invalid_value, "tuple")

        will_raise_value_errors = [None, ()]
        for invalid_value in will_raise_value_errors:
            with self.subTest(
                    msg="Test values that will raise a ValueError exception " +
                    "with 'validate_int_tuple_property' for the 'value' " +
                    " parameter.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    val.validate_int_tuple_property(invalid_value, "tuple")
        # property_name parameter - string
        will_raise_type_errors_for_property_name = [1, 2.2, [2, 3], {}, (),
                                                    self.dt]
        for invalid_value in will_raise_type_errors_for_property_name:
            with self.subTest(
                    msg="Test values that will raise a TypeError exception " +
                    "with 'validate_int_tuple_property' for the " +
                    "'property_name' parameter.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    val.validate_int_tuple_property((1, 2, 3), invalid_value)
        will_raise_value_errors_for_property_name = [None, "", " "]
        for invalid_value in will_raise_value_errors_for_property_name:
            with self.subTest(
                    msg="Test values that will raise a ValueError exception " +
                    "with 'validate_int_tuple_property' function for the " +
                    "'property_name' parameter",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    val.validate_int_tuple_property((1, 2, 3), invalid_value)

    def test_validate_string_dict_property_successful(self):
        print("=== test_validate_string_dict_successful ===")
        test_dict = {"dict": "test"}
        prop_value = "test_dict"
        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict, {"dict": "test"})
        self.assertIsInstance(prop_value, str)
        self.assertEqual(prop_value, "test_dict")

    def test_validate_string_dict_property_failure_value_parameter(self):
        t_name = "test_validate_string_dict_property_failure_value_parameter"
        print(f"=== {t_name} ===")
        # ValueError
        raises_value_errors = [None, " ", ""]
        for invalid_value in raises_value_errors:
            with self.subTest(
                    msg="Test values that will raise a ValueError exception " +
                    "with the 'validate_string_dict_property' function for " +
                    " the 'value' parameter.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    val.validate_string_dict_property(
                            {invalid_value: invalid_value}, "test_dict")

        # TypeError
        raises_type_errors = [[], {}, 10, 1.3, (1, 2)]
        for invalid_value in raises_type_errors:
            with self.subTest(
                    msg="Test values that will raise a TypeError exception " +
                    " with 'validate_string_dict_property' function for  " +
                    "the 'value' parameter.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    val.validate_string_dict_property(
                            {invalid_value, invalid_value}, "test_dict")

    def test_validate_string_dict_property_failure_property_value(self):
        t_name = "test_validate_string_dict_property_failure_property_value"
        print(f"=== {t_name} ===")
        raises_value_errors = [None, " ", ""]

        # ValueError
        for invalid_value in raises_value_errors:
            with self.subTest(
                    msg="Test values that will raise a ValueError exception " +
                    "with the 'validate_string_dict_property' function for " +
                    " the 'property_name' parameter.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    val.validate_string_dict_property(
                            {"test": "test_dict"}, invalid_value)

        # TypeError
        raises_type_errors = [[], {}, 10, 1.3, (1, 2)]
        for invalid_value in raises_type_errors:
            with self.subTest(
                    msg="Test values that will raise a TypeError exception " +
                    "with the 'validate_string_dict_property' function for " +
                    "'property_name' parameter.",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    val.validate_string_dict_property(
                            {"test": "test_dict"}, invalid_value)


if __name__ == '__main__':
    unittest.main()
