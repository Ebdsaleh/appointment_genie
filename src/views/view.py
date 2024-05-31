# src/views/view.py
import tkinter as tk
from tkinter import ttk
from src.utils.validators import validate_string_property, \
    validate_int_tuple_property


class View:

    """
    This class will be used a template for creating views or forms and other
    GUI objects.
    """

    def __init__(self, title="new_view", size=(300, 400)):
        if title is None:
            self._title = "new_view"
        else:
            self._title = title
        if size is None:
            self._size = (300, 400)
        else:
            self._size = size
        self._width = size[0]
        self._height = size[1]
        self.components = []

        # Set up the Tkinter window
        self.tk = tk.Tk()
        self.tk.title(self._title)
        self.tk.geometry(f"{self._size[0]}x{self._size[1]}")

# properties
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        validate_string_property(value, 'title')
        self._title = value
        if hasattr(self, 'tk'):
            self.tk.title(self._title)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        validate_int_tuple_property(value, 'size')
        if not len(value) == 2 and all(isinstance(dim, int) for dim in value):
            raise ValueError(
                    "'size' must be a tuple of two integers (width, height).")
        self._size = value
        self._width, self._height = value
        if hasattr(self, 'tk'):
            self.tk.geometry(f"{self._width}x{self._height}")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value is None:
            raise ValueError("'width must not be None.'")
        if not isinstance(value, int):
            raise TypeError("'width' must be an int.")
        self._width = value
        self._size = (self._width, self._height)
        if hasattr(self, 'tk'):
            self.tk.geometry(f"{self._width}x{self._height}")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value is None:
            raise ValueError("'height' must not be None.")
        if not isinstance(value, int):
            raise TypeError("'height' must be an int.")
        self._height = value
        self._size = (self._width, self.height)
        if hasattr(self, 'tk'):
            self.tk.geometry(f"{self._width}x{self._height}")
