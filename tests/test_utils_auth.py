# test/test_utils_auth.py
import unittest
from src.utils.auth import generate_pw_hash, verify_password


class TestAuth(unittest.TestCase):

    def setUp(self):
        print("Testing '/src/utils/auth.py'")
        self.pw = "password"
        self.pw_hash = generate_pw_hash(self.pw)
        self.generic_string_type_error_values = [
                1, 2.2, [2, 3], {}, ()]

    def tearDown(self):
        print("End of testing 'src/utils/auth.py'")

    def test_verify_password_success(self):
        print("=== test_verify_password_success ===")
        self.assertIsInstance(verify_password(self.pw_hash, self.pw), bool)
        self.assertTrue(verify_password(self.pw_hash, self.pw))

    def test_verify_password_failure_parameter_pw_hash(self):
        print("=== test_verify_password_pw_hash_failure ===")
        raises_value_errors = [None, "", ' ']
        raises_type_errors = self.generic_string_type_error_values

        # pw_hash ValueError
        for invalid_value in raises_value_errors:
            with self.subTest(
                    msg="Test values that will raise a ValueError exception " +
                    "for the 'pw_hash' parameter in the 'verify_password' " +
                    "function.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    verify_password(invalid_value, self.pw)

        # pw_hash TypeError
        for invalid_value in raises_type_errors:
            with self.subTest("Test values that will raise a TypeError " +
                              "exception for the 'pw_hash' parameter in the " +
                              "'verify_password' function. ",
                              value=invalid_value):
                with self.assertRaises(TypeError):
                    verify_password(invalid_value, self.pw)

    def test_verify_password_failure_parameter_password(self):
        print("=== test_verify_password_failure_parameter_password ===")
        raises_value_errors = [None, "", ' ']
        raises_type_errors = self.generic_string_type_error_values

        # password ValueError
        for invalid_value in raises_value_errors:
            with self.subTest(
                    msg="Test values that will raise a ValueError " +
                    "exception for the 'password' parameter in the " +
                    "'verify_password_function'.",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    verify_password(self.pw_hash, invalid_value)

        # password TypeError
        for invalid_value in raises_type_errors:
            with self.subTest(
                    msg="Test values that will raise a TypeError " +
                    "exception for the 'password' parameter in the " +
                    "'verify_password' function",
                    value=invalid_value):
                with self.assertRaises(TypeError):
                    verify_password(self.pw_hash, invalid_value)

    def test_generate_pw_hash_success(self):
        print("=== test_generate_pw_hash_success")
        self.assertIsInstance(self.pw, str)
        self.assertTrue(verify_password(self.pw_hash, self.pw))

    def test_generate_pw_hash_failure(self):
        print("=== test_generate_pw_hash_failure ===")
        raises_value_errors = [None, "", ' ']
        raises_type_errors = self.generic_string_type_error_values

        # Test for ValueError
        for invalid_value in raises_value_errors:
            with self.subTest(
                    msg="Test values that will raise a ValueError exception " +
                    " for the 'generate_pw_hash' function. ",
                    value=invalid_value):
                with self.assertRaises(ValueError):
                    generate_pw_hash(invalid_value)

        # Test for TypeError
        for invalid_value in raises_type_errors:
            with self.subTest("Test values that will raise a TypeError " +
                              "execption for the 'generate_pw_hash' function.",
                              value=invalid_value):
                with self.assertRaises(TypeError):
                    generate_pw_hash(invalid_value)


if __name__ == '__main__':
    unittest.main()
