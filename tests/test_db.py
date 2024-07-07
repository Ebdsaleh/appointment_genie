# tests/test_db.py
import unittest
import sqlite3
from src.db import db


class TestDb(unittest.TestCase):

    def setUp(self):
        print("TestDb setUp")
        self.db = db
        self.db_name = "test.db"
        self.users_table_schema = """
            users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """
        self.insert_query = "INSERT INTO users(username, password, email)" + \
            " VALUES (?, ?, ?)"
        self.user_data = (
                "test_user",
                "password",
                "test_email@email.com"
                )

        if self.db.connection:
            self.db.close()

    def test_db_connection(self):
        print("=== test_db_connection ===")
        self.assertIsNone(self.db.connection)
        self.db.create_connection(self.db_name)
        self.assertIsInstance(self.db.connection, sqlite3.Connection)
        if self.db.table_exists(self.db.cursor, "users"):
            self.db.cursor.execute("DROP TABLE users")
            self.db.commit()
        self.db.commit()
        self.db.close()

    def test_db_cursor(self):
        print("=== test_db_cursor ===")
        self.db.create_connection(self.db_name)
        self.assertIsNotNone(self.db.cursor)
        self.db.close()

    def test_db_db_name(self):
        print("=== test_db_db_name ===")
        self.assertIsNotNone(self.db.db_name)
        self.assertEqual(self.db.db_name, self.db_name)

    def test_db_create_connection(self):
        print("=== test_db_create_connection ===")
        test_conn = self.db.create_connection(self.db_name)
        self.assertEqual(self.db.db_name, self.db_name)
        self.assertIsInstance(test_conn, sqlite3.Connection)
        self.assertEqual(self.db.connection, test_conn)

        # Ensure Connection is open
        self.assertFalse(test_conn is None)

        # Ensure the connection is open by trying to create a cursor
        try:
            cursor = test_conn.cursor()
            cursor.execute("SELECT 1")
        except sqlite3.Error as e:
            self.fail(f"Connection seems to be closed or invalid: {e}")
        # Close Database
        self.db.close()
        test_conn.close()
        test_conn = None

        # ValueError tests
        raises_value_errors = [None, "", " "]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values that raise a ValueError exception with the " +
                "'_db_name' parameter.",
                value=invalid_value
            ):
                with self.assertRaises(ValueError):
                    self.db.create_connection(invalid_value)
        # TypeError tests
        raises_type_errors = [1, 1.0, [], {}, self.db, (), (1, 2, " ")]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception with the " +
                "'_db_name' parameter.",
                value=invalid_value
            ):
                with self.assertRaises(TypeError):
                    self.db.create_connection(invalid_value)

    def test_db_get_cursor(self):
        print("=== test_get_cursor ===")
        self.db.create_connection(self.db_name)
        self.assertIsNotNone(self.db.get_cursor())
        self.assertIsInstance(self.db.get_cursor(), sqlite3.Cursor)
        self.assertIsNotNone(self.db.cursor)
        self.assertIsInstance(self.db.cursor, sqlite3.Cursor)
        self.db.close()

    def test_db_create_table_query(self):
        guard = "CREATE TABLE IF NOT EXISTS "
        table_schema = self.users_table_schema
        result = self.db.create_table_query(self.users_table_schema)

        self.assertIsNotNone(
                self.db.create_table_query(self.users_table_schema)
                )
        self.assertEqual(
                self.db.create_table_query(self.users_table_schema), result)
        self.assertEqual(result, str(guard + table_schema))
        # ValueError tests
        raises_value_errors = [None, " ", ""]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values that raise a ValueError exception with the " +
                "'table_definition' property."
            ):
                with self.assertRaises(ValueError):
                    self.db.create_table_query(invalid_value)
        # TypeError tests
        raises_type_errors = [
                2, 1.2, (1, 3, 4), ["Select FROM", 12], {"user": "value"},
                self.db]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception with the " +
                "'table_definition' parameter.",
                value=invalid_value
            ):
                with self.assertRaises(TypeError):
                    self.db.create_table_query(invalid_value)

    def test_db_create_table(self):
        print("=== test_create_table ===")
        table_query = self.db.create_table_query(self.users_table_schema)
        table_name = "users"
        self.db.create_connection(self.db_name)
        self.db.create_table(self.db.cursor, table_query)
        self.assertTrue(self.db.table_exists(self.db.cursor, table_name))
        self.db.commit()
        self.db.close()

    def test_db_commit(self):
        print("=== test_db_commit ===")
        self.db.create_connection(self.db_name)
        query = self.db.create_table_query(self.users_table_schema)
        self.db.create_table(self.db.cursor, query)
        self.assertTrue(self.db.commit())
        self.db.close()

    def test_db_close(self):
        print("=== test_db_close ===")
        self.db.create_connection(self.db_name)
        self.assertTrue(self.db.close())
        self.assertIsNone(self.db.connection)
        self.assertIsNone(self.db.cursor)
        if self.db.connection:
            self.db.close()

    def test_db_get_users(self):
        print("=== test_db_get_users ===")
        self.db.create_connection(self.db_name)
        users = self.db.get_users(self.db.cursor)
        self.assertIsNone(users)
        self.assertTrue(
                self.db.insert(
                    self.db.cursor, self.insert_query, self.user_data)
                )
        users = self.db.get_users(self.db.cursor)
        self.assertIsNotNone(users)
        self.assertIsInstance(users, list)
        self.db.close()

    def test_db_show_tables(self):
        print("=== test_db_show_tables ===")
        self.db.create_connection(self.db_name)
        self.assertTrue(self.db.show_tables())
        self.db.close()

    def test_db_table_exists(self):
        print("=== test_db_table_exists")
        self.db.create_connection(self.db_name)
        table_name = "users"
        self.assertTrue(self.db.table_exists(self.db.cursor, table_name))
        self.db.close()
        # ValueError tests
        raises_value_errors = [None, "", " "]
        for invalid_value in raises_value_errors:
            with self.subTest(
                msg="Test values that raise a ValueError exception with the " +
                "'table_name' parameter.",
                value=invalid_value
            ):
                with self.assertRaises(ValueError):
                    self.db.table_exists(self.db.cursor, invalid_value)
        # TypeError tests
        raises_type_errors = [
                1, 2.3, (3, 3, "hello"), ["undefined", 12, self.db], {}, [],
                self.db
                ]
        for invalid_value in raises_type_errors:
            with self.subTest(
                msg="Test values that raise a TypeError exception with the " +
                "'table_definition' parameter",
                value=invalid_value
            ):
                with self.assertRaises(TypeError):
                    self.db.table_exists(self.db.cursor, invalid_value)

    def tearDown(self):
        print("TestDb tearDown")
        if self.db.connection:
            self.db.close()
        self.db = None


if __name__ == '__main__':
    unittest.main()
