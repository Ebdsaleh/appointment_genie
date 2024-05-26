# tests/test_main.py
import src.main
import unittest


class TestMain(unittest.TestCase):
    def test_run_main_successful(self):
        print("TestMain is running")
        src.main.main()


if __name__ == '__main__':
    unittest.main()
