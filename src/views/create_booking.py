# views/create_booking.py
from src.views.view import View, DateEntry
import tkinter as tk
from tkinter import ttk as ttk
import datetime


class CreateBooking(View):
    def __init__(self, controller, title="Create Booking", size=(420, 400)):
        super().__init__(title=title, size=size)
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        self.create_label(
                name="lbl_create_booking", x=150, y=20,
                text="Create Booking"
                )
        self.create_label(
                name="lbl_contact", x=20, y=80,
                text="Contact:"
                )
        self.create_label(
                name="lbl_time", x=20, y=120,
                text="Time:"
                )
        self.create_label(
                name="lbl_date", x=20, y=160,
                text="Date:"
                )
        # To be replaced by other objects, will start with text fields.object
        self.create_dropdown(
                name="cmb_contact", x=150, y=80,
                width=20
                )
        self.create_spinbox(
                name="spinbox_hour", x=150, y=120,
                width=3, from_=0, to=23, increment=1
                )
        self.create_spinbox(
                name="spinbox_minute", x=200, y=120,
                width=3, from_=0, to=59, increment=1
                )
        self.create_calender(
                name="calendar", x=150, y=160,
                width=20
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
        self.set_font("lbl_create_booking", "Arial", 18,
                      ("bold", "roman", "no_underline"))
        self.set_font("lbl_contact", "Arial", 14,
                      ("normal", "roman", "no_underline"))
        self.set_font("lbl_time", "Arial", 14,
                      ("normal", "roman", "no_underline"))
        self.set_font("lbl_date", "Arial", 14,
                      ("normal", "roman", "no_underline"))

    def submit(self):
        details = []
        for component in self.components:
            for widget in component.values():
                if isinstance(widget, ttk.Combobox):
                    details.append(widget.textvariable.get())
                if isinstance(widget, tk.Spinbox):
                    details.append(widget.numvar.get())
                if isinstance(widget, DateEntry):
                    details.append(widget.get_date())
        self.controller.handle_create_booking(details)
        return details

    def clear(self):
        for component in self.components:
            for widget in component.values():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
                if isinstance(widget, DateEntry):
                    new_date = datetime.datetime.now()
                    widget.set_date(datetime.date(
                        new_date.year,
                        new_date.month,
                        new_date.day))
                if isinstance(widget, tk.Spinbox):
                    widget.textvariable.set(0)
                    widget.numvar.set(0)


if __name__ == '__main__':
    pass
