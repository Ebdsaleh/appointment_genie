# controller.py
from src.user.user import User
from src.views.login import Login


class Controller:
    """
        This class will handle the switch between views and program flow.
    """

    def __init__(self):
        self.user = User()
        self.login_view = Login(controller=self)
        self.login_view.mainloop()

    def handle_login(self, username, password):
        if self.user.authenticate(username, password):
            print("Login successful.")
        else:
            print("Login failed.")


if __name__ == '__main__':
    Controller()
