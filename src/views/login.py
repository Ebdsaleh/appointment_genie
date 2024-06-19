# src/views/login.py
from src.views.view import View


class Login(View):
    """
    This class will allow the user to log into the application.
    derives from: View

    """

    def __init__(self, controller, title="Login", size=(300, 400)):
        self.controller = controller
        super().__init__(title=title, size=size)
        self.setup_ui()

    def setup_ui(self):
        self.create_label(name="lbl_login", x=110, y=80, text="Login")
        self.create_label(name="lbl_username", x=20, y=130, text="Username:")
        self.create_label(name="lbl_password", x=20, y=180, text="Password:")
        self.create_entry_text_field(
                name="txt_username", x=120, y=130, width=170)
        self.create_entry_text_field(
                name="txt_password", x=120, y=180, width=170, show="*")
        self.create_button(
                name="btn_submit", text="Submit",
                x=210, y=230,
                command=self.submit)
        # make it look prettier
        self.set_font(
                "lbl_login", "Arial", 18,
                ("bold", "roman", "no_underline"))
        self.set_font(
                "lbl_username", "Arial", 14,
                ("normal", "roman", "no_underline"))
        self.set_font(
                "lbl_password", "Arial", 14,
                ("normal", "roman", "no_underline"))
        self.set_font(
                "btn_submit", "Arial", 14,
                ("normal", "roman", "no_underline"))

    def submit(self):
        """
        This method (at the moment) the entered password inside the
        'txt_passeword' 'entry_text_field'. It is bound to the 'btn_submit'
        tk.Button.
        I'm thinking there needs to be a event manager to handle GUI events,
        this will allow forms/views to change in fluid manner."""
        username = self.get_component('txt_username').get()
        pw = self.get_component('txt_password').get()
        self.controller.handle_login(username, pw)
        return pw


if __name__ == '__main__':
    pass
