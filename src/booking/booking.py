# src/booking/booking.py
from datetime import datetime
from src.utils.validators import validate_string_property, \
        validate_datetime_property, validate_int_tuple_property


def validate_date_property(value):
    validate_datetime_property(value, "date")


def validate_time_property(value: tuple):
    # Should receive an int tuple(hour, minute)
    validate_int_tuple_property(value, "time")
    if value[0] < 0 or value[0] > 23:
        raise ValueError(
                "'hour' must not be less than 0 or greater than 23.\n" +
                f"received: {value[0]}")
    elif value[1] < 0 or value[1] > 59:
        raise ValueError(
                "'minute' must not be less than 0 or greater than 59.\n" +
                f"recieved: {value[1]}")


class Booking:

    def __init__(self, _title="New Booking",
                 _date=None,
                 _time=None,
                 _contact="New Contact",
                 _description="Enter a description."):
        if _date is None:
            dt = datetime.now()
            _date = (dt.year, dt.month, dt.day)

        if _time is None:
            dt = datetime.now()
            _time = (dt.hour, dt.minute)

        self._title = _title
        self._date = _date
        self._time = _time
        self._contact = _contact
        self._description = _description

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        validate_string_property(value, "title")
        self._title = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        validate_date_property(value)
        self._date = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        validate_time_property(value)
        self._time = value

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        validate_string_property(value, "contact")
        self._contact = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        validate_string_property(value, "description")
        self._description = value

    def __repr__(self):
        return (f"Booking(title='{self.title}', "
                f"date={self.date}, "
                f"time={self.time}, "
                f"contact='{self.contact}', "
                f"description='{self.description}')")
