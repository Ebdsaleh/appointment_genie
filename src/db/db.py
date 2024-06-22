# src/db/db.py
import sqlite3

connection = None
cursor = None
db_name = None


def create_connection(_db_name):
    global connection, cursor, db_name
    connection = sqlite3.connect(_db_name)
    cursor = connection.cursor()
    db_name = _db_name
    return connection


def get_cursor():
    if cursor is None:
        print("Error getting db cursor")
        return None
    else:
        return cursor


def create_table_query(table_definition):
    guard = "CREATE TABLE IF NOT EXISTS "
    return guard + table_definition


def create_table(cursor, query):
    try:
        cursor.execute(query)
        print(f"Table created sucessfully.\n{query}")
    except sqlite3.Error as e:
        print("Error creating table", e)


def commit():
    try:
        connection.commit()
        return True
    except sqlite3.Error as e:
        print("Error when trying to commit.", e)
        return False


def close():
    global connection, cursor
    try:
        connection.close()
        print("db connection closed.")
        connection, cursor = None, None
        return True
    except sqlite3.Error as e:
        print("No connection open, close() command aborted.", e)
        return False


def insert(cursor, insert_query, data):
    try:
        cursor.execute(insert_query, data)
        commit()  # Commit the transaction
        return True
    except sqlite3.Error as e:
        print("Error when trying to insert", e)
        return False


def get_users(cursor):
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    if not users:
        return None
    else:
        return list(users)


def show_tables():
    try:
        cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table';"
                )
        tables = cursor.fetchall()
        print("tables in the database:")
        for table in tables:
            print(table[0])
        return True
    except sqlite3.Error as e:
        print("Error fetching tables", e)
        return False


def table_exists(cursor, table_name):
    try:
        cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND " +
                " name=?", (table_name,)
                )
        result = cursor.fetchone()
        return result is not None
    except sqlite3.Error as e:
        print("Error checking if table exists", e)
        return False


if __name__ == '__main__':
    print("not intended to run in isolation")
