# src/main.py
from src.controller.controller import Controller
import src.db.db as db


def main():
    db_name = "app_genie.db"
    table_schema = """
        users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
                )"""
    db.create_connection(_db_name=db_name)
    db_query = db.create_table_query(table_schema)
    db.create_table(db.cursor, db_query)
    db.show_tables()
    print("Welcome To Appointment Genie!")
    controller = Controller()
    view = controller.handle_login_view(title="App Genie: Login")
    view.tk.mainloop()


if __name__ == '__main__':
    main()
