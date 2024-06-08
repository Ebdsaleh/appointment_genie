# tests/test_view_create_booking.py
import unittest
import tkinter as tk
import tkinter.ttk as ttk
import datetime
from src.views.view import View, DateEntry
from src.views.create_booking import CreateBooking


class TestViewCreateBooking(unittest.TestCase):

    def setUp(self):
        self.create_booking = CreateBooking()
        self.component_names = [
                name for component in self.create_booking.components
                for name in component.keys()]
        self.widgets = [
                ttk.Frame, ttk.Label, ttk.Label, ttk.Label, ttk.Label,
                ttk.Combobox, tk.Spinbox, tk.Spinbox, DateEntry, tk.Button,
                tk.Button]

    def test_view_create_default_paramters(self):
        print("=== test_view_create_default_paramters ===")
        self.assertIsInstance(self.create_booking, CreateBooking)
        self.assertIsInstance(self.create_booking, View)
        self.assertTrue(issubclass(CreateBooking, View))
        self.assertEqual(self.create_booking.title, "Create Booking")
        self.assertEqual(self.create_booking.size, (420, 400))
        for i, name in enumerate(self.component_names):
            self.assertIsInstance(
                    self.create_booking.get_component(name),
                    self.widgets[i]
                    )

    def test_submit(self):
        print("=== test_submit ===")
        contact_text = "Option 1"
        time_tuple = (14, 20)
        date_text = "9/6/24"
        contact_dropdown = self.create_booking.get_component("cmb_contact")
        time_hour = self.create_booking.get_component("spinbox_hour")
        time_minute = self.create_booking.get_component("spinbox_minute")
        calendar = self.create_booking.get_component("calendar")
        contact_dropdown.textvariable.set(contact_text)
        time_hour.textvariable.set(time_tuple[0])
        time_hour.numvar.set(time_tuple[0])
        time_minute.textvariable.set(time_tuple[1])
        time_minute.numvar.set(time_tuple[1])
        calendar.set_date(date_text)

        self.assertEqual(contact_dropdown.get(), contact_text)
        self.assertEqual(time_hour.get(), str(time_tuple[0]))
        self.assertEqual(time_minute.get(), str(time_tuple[1]))
        self.assertEqual(time_hour.numvar.get(), time_tuple[0])
        self.assertEqual(time_minute.numvar.get(), time_tuple[1])
        self.assertEqual(calendar.get_date(), datetime.date(2024, 6, 9))
        details = self.create_booking.submit()
        self.assertEqual(details, [
            'Option 1', 14, 20, datetime.date(2024, 6, 9)])

    def test_clear(self):
        print("=== test_clear ===")
        contact_text = "test contact"
        time_tuple = (14, 20)
        date_text = "9/6/24"
        contact_dropdown = self.create_booking.get_component("cmb_contact")
        time_hour = self.create_booking.get_component("spinbox_hour")
        time_minute = self.create_booking.get_component("spinbox_minute")
        calendar = self.create_booking.get_component("calendar")
        contact_dropdown.textvariable.set(contact_text)
        time_hour.textvariable.set(time_tuple[0])
        time_minute.textvariable.set(time_tuple[1])
        time_hour.numvar.set(time_tuple[0])
        time_minute.numvar.set(time_tuple[1])
        calendar.set_date(date_text)

        self.assertEqual(contact_dropdown.get(), contact_text)
        self.assertEqual(time_hour.get(), str(time_tuple[0]))
        self.assertEqual(time_minute.get(), str(time_tuple[1]))
        self.assertEqual(time_hour.numvar.get(), time_tuple[0])
        self.assertEqual(time_minute.numvar.get(), time_tuple[1])
        self.assertEqual(calendar.get_date(), datetime.date(2024, 6, 9))
        new_date = datetime.datetime.now()
        self.create_booking.clear()
        self.assertEqual(contact_dropdown.get(), '')
        self.assertEqual(time_hour.get(), '0')
        self.assertEqual(time_minute.get(), '0')
        self.assertEqual(time_hour.numvar.get(), 0)
        self.assertEqual(time_minute.numvar.get(), 0)
        self.assertEqual(calendar.get_date(), datetime.date(new_date.year,
                                                            new_date.month,
                                                            new_date.day))

    def tearDown(self):
        self.create_booking.components = None
        self.create_booking.tk.destroy()
        self.create_booking = None


if __name__ == '__main__':
    unittest.main()
