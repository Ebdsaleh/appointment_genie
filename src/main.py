# src/main.py
from src.views.login import Login


def main():
    print("Welcome To Appointment Genie!")
    login = Login(title="App Genie: Login")
    login.tk.mainloop()


if __name__ == '__main__':
    main()
