# src/views/view.py
import tkinter as tk
from tkinter import ttk
from src.utils.validators import validate_string_property, \
    validate_int_tuple_property, validate_int_property


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
        validate_int_property(value, 'width')
        self._width = value
        self._size = (self._width, self._height)
        if hasattr(self, 'tk'):
            self.tk.geometry(f"{self._width}x{self._height}")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        validate_int_property(value, 'height')
        self._height = value
        self._size = (self._width, self.height)
        if hasattr(self, 'tk'):
            self.tk.geometry(f"{self._width}x{self._height}")

    # components
    def create_button(self, name="button", text="Click me", padx=0, pady=0):
        validate_string_property(name, 'name')
        validate_string_property(text, 'text')
        validate_int_property(padx, 'padx')
        validate_int_property(pady, 'pady')
        button = ttk.Button(self.tk, text=text)
        button.name = name
        button.pack(padx=padx, pady=pady)
        self.components.append({name: button})
        return button

    def get_component(self, component_name):
        validate_string_property(component_name, 'component_name')
        for component in self.components:
            for k, v in component.items():
                if k == component_name:
                    return v
        return None

    def create_label(self, name='label', text="new label"):
        validate_string_property(name, 'name')
        validate_string_property(text, 'text')
        label = ttk.Label(self.tk, text=text)
        label.name = name
        label.pack()
        self.components.append({name: label})
        return label

    def create_entry_text_field(
            self, name="entry_text_field", width=30):
        validate_string_property(name, 'name')
        validate_int_property(width, 'width')
        if width < 11:
            raise ValueError("'width' must be greater than 10")
        entry_text_field = tk.Entry(self.tk, width=width)
        entry_text_field.name = name
        entry_text_field.pack()
        self.components.append({name: entry_text_field})
        return entry_text_field

    def create_frame(
            self, name="main_frame",
            x=0, y=0,
            width=100, height=100, **kwargs):
        validate_string_property(name, 'name')
        validate_int_property(x, 'x')
        validate_int_property(y, 'y')
        validate_int_property(width, 'width')
        validate_int_property(height, 'height')
        frame = ttk.Frame(self.tk, **kwargs)
        frame.place(x=x, y=y, width=width, height=height)
        frame.name = name
        self.components.append({frame.name: frame})
        return frame

