# src/main.py
from src.controller.controller import Controller


def main():
    print("Welcome To Appointment Genie!")
    controller = Controller()
    view = controller.handle_login_view(title="App Genie: Login")
    view.tk.mainloop()


if __name__ == '__main__':
    main()
