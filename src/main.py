# src/main.py
from src.views.add_contact import AddContact


def main():
    print("Welcome To Appointment Genie!")
    add_contact = AddContact(title="App Genie: Add Contact")
    add_contact.tk.mainloop()


if __name__ == '__main__':
    main()
