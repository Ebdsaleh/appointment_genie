# src/views/view.py
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from src.utils.validators import validate_string_property, \
    validate_int_tuple_property, validate_int_property, \
    validate_string_tuple_property


class View:

    """
    This class will be used a template for creating views or forms and other
    GUI objects.
    """

    def __init__(self, title="new_view", size=(300, 400)):
        self.title = title if title is not None else "new_view"
        self.size = size if size is not None else (300, 400)
        self._width = size[0]
        self._height = size[1]
        self.components = []

        # Set up the Tkinter window
        self.tk = tk.Tk()
        self.tk.title(self._title)
        self.tk.geometry(f"{self._size[0]}x{self._size[1]}")
        # create the frame to place widgets
        self.frame = self.create_frame(
                name="main_frame", x=0, y=0,
                width=self.width, height=self.height)

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
            self.frame.place(width=self._width, height=self._height)

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
            self.frame.place(width=self._width, height=self._height)

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
            self.frame.place(width=self._width, height=self._height)

    # components
    def create_button(
            self,
            name="button",
            text="Click me",
            x=0, y=0,
            command=None,
            parent=None):
        validate_string_property(name, 'name')
        validate_string_property(text, 'text')
        validate_int_property(x, 'x')
        validate_int_property(y, 'y')
        parent = parent or self.frame
        button = tk.Button(parent, text=text, command=command)
        button.name = name
        button.command = command
        button.place(x=x, y=y)
        self.components.append({name: button})
        font_family = "Arial"
        font_size = 9
        font_style = ("normal", "roman", "no_underline")
        button.font = [
                {"family": font_family}, {"size": font_size},
                {"weight": "bold" if font_style[0] == "bold" else "normal"},
                {"slant": "italic" if font_style[1] == "italic" else "roman"},
                {"underline": 1 if font_style[2] == "underline" else 0}
                ]
        self.set_font(
                component_name=name, font_family=font_family,
                font_size=font_size,
                font_style=font_style)
        return button

    def get_component(self, component_name):
        validate_string_property(component_name, 'component_name')
        for component in self.components:
            for k, v in component.items():
                if k == component_name:
                    return v
        return None

    def create_label(
            self, name='label', text="new label", x=0, y=0, parent=None):
        validate_string_property(name, 'name')
        validate_string_property(text, 'text')
        validate_int_property(x, 'x')
        validate_int_property(y, 'y')
        parent = parent or self.frame
        label = ttk.Label(parent, text=text)
        label.name = name
        label.place(x=x, y=y)
        self.components.append({name: label})
        font_family = "Arial"
        font_size = 9
        font_style = ("normal", "roman", "no_underline")
        label.font = [
                {"family": font_family}, {"size": font_size},
                {"weight": "bold" if font_style[0] == "bold" else "normal"},
                {"slant": "italic" if font_style[1] == "italic" else "roman"},
                {"underline": 1 if font_style[2] == "underline" else 0}
                ]
        self.set_font(name, font_family, font_size, font_style)
        return label

    def create_entry_text_field(
            self, name="entry_text_field", width=30,
            x=0, y=0, show=None, parent=None):
        validate_string_property(name, 'name')
        validate_int_property(width, 'width')
        if width < 11:
            raise ValueError("'width' must be greater than 10")
        validate_int_property(x, 'x')
        validate_int_property(y, 'y')
        parent = parent or self.frame
        entry_text_field = tk.Entry(parent, width=width, show=show)

        entry_text_field.name = name
        entry_text_field.show = show
        entry_text_field.place(x=x, y=y, width=width)
        self.components.append({name: entry_text_field})
        font_family = "Arial"
        font_size = 9
        font_style = ("normal", "roman", "no_underline")
        entry_text_field.font = [
                {"family": font_family}, {"size": font_size},
                {"weight": "bold" if font_style[0] == "bold" else "normal"},
                {"slant": "italic" if font_style[1] == "italic" else "roman"},
                {"underline": 1 if font_style[2] == "underline" else 0}
                ]
        self.set_font(name, font_family, font_size, font_style)
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

    def set_font(
            self, component_name,
            font_family, font_size=10,
            font_style=(
                "normal",
                "roman",
                "no_underline")
            ):
        """
            This method will set the font for Labels, and Buttons.
            It also returns the component that the font is being applied to.
            Returns None if the component doesn't exist in the self.components
            list.
            parameters:
                component_name: str
                font_family: str
                font_size: int
                font_style: tuple (str, str, str)
            expected exceptions:
                ValueError
                TypeError
            """
        validate_string_property(component_name, 'component_name')
        validate_string_property(font_family, 'font_family')
        validate_int_property(font_size, 'font_size')
        validate_string_tuple_property(font_style, 'font_style')

        # Check if component exists
        component = self.get_component(component_name)
        if component is None:
            raise ValueError(
                    f"Could not find {component_name} in the component list.")

        fonts = ["Arial", "Courier", "Helvetica", "Times", "Verdana"]
        # Ensure font_style has the right number of elements
        if len(font_style) > 3:
            raise ValueError(
                    "'font_style' must be a tuple of up to 3 elements.")
        # Extend font_style to have 3 elements, filling in the defaults
        default_styles = ["normal", "roman", "no_underline"]
        font_style = tuple(font_style) + tuple(
                default_styles[len(font_style):])

        # Validate each style
        valid_styles = {"weight": ["normal", "bold"],
                        "slant": ["roman", "italic"],
                        "underline": ["no_underline", "underline"]}
        for i, style in enumerate(font_style):
            if style not in valid_styles[list(valid_styles.keys())[i]]:
                raise ValueError(f"Invalid value for font_style {style}")

        # Check if font is supported
        if font_family not in fonts:
            raise ValueError(
                    f"Could not find {font_family}, in supported font list.")

        # Define a style
        font = tkFont.Font(
                family=font_family, size=font_size,
                weight=font_style[0],
                slant=font_style[1],
                underline=1 if font_style[2] == "underline" else 0
                )

        # Apply the font
        if isinstance(component, (tk.Button, ttk.Label, tk.Entry)):
            component.configure(font=font)
        else:
            raise TypeError(
                    f"Font setting not supported for {type(component)}.")

        component.font = [
                {"family": font_family}, {"size": font_size},
                {"weight": font_style[0]},
                {"slant": font_style[1]},
                {"underline": 1 if font_style[2] == "underline" else 0}
        ]
        return component
