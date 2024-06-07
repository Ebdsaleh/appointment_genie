# views/add_contact.py
from src.views.view import View
import tkinter as tk


class AddContact(View):
    def __init__(self, title="Add Contact", size=(420, 400)):
        super().__init__(title=title, size=size)
        self.setup_ui()

    def setup_ui(self):
        self.create_label(
                name="lbl_add_contact",
                x=170, y=20, text="Add Contact")

        self.create_label(
                name="lbl_name", x=20, y=80,
                text="Contact Name:"
                )

        self.create_label(
                name="lbl_email", x=20, y=120,
                text="Contact Email:"
                )

        self.create_entry_text_field(
                name="txt_contact_name", x=150, y=80,
                width=170
                )

        self.create_entry_text_field(
                name="txt_contact_email", x=150, y=120,
                width=170
                )

        self.create_button(
                name="btn_submit", x=210, y=230,
                text="Submit", command=self.submit
                )

        self.create_button(
                name="btn_clear", x=150, y=230,
                text="Clear", command=self.clear
                )

        # Make it look prettier
        self.set_font("lbl_add_contact", "Arial", 18,
                      ("bold", "roman", "no_underline"))
        self.set_font("lbl_name", "Arial", 14,
                      ("normal", "roman", "no_underline"))
        self.set_font("lbl_email", "Arial", 14,
                      ("normal", "roman", "no_underline"))
        self.set_font("btn_submit", "Arial", 14,
                      ("normal", "roman", "no_underline"))
        self.set_font("btn_clear", "Arial", 14,
                      ("normal", "roman", "no_underline"))

    def submit(self):
        print("AddContact.submit()")
        details = []
        for component in self.components:
            for widget in component.values():
                if isinstance(widget, tk.Entry):
                    details.append(widget.get())
        return details

    def clear(self):
        print("AddContact.clear()")
        for component in self.components:
            for widget in component.values():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
