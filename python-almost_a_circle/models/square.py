#!/usr/bin/python3
"""Here is the module description"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Description of the the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns formatted string"""
        coordinates = f"{self.x}/{self.y}"
        return f"[Square] ({self.id}) {coordinates} - {self.width}"

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """"Sets the size value with validation"""
        self.width = type(self).dimension_validator(self, "width", value)
        self.height = type(self).dimension_validator(self, "height", value)

    def dimension_validator(self, name, value):
        """"Validates the width and height values as positive integers"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))
        else:
            return value

    def coordinate_validator(self, name, value):
        """"Validates the x and y values as positive integers"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))
        else:
            return value

    def update(self, *args, **kwargs):
        """Updates attributes of instance"""
        attribute_list = ["id", "size", "x", "y"]
        for arg in args:
            try:
                setattr(self, attribute_list[args.index(arg)], arg)
            except KeyError:
                pass
        for kwarg in kwargs:
            try:
                setattr(self, kwarg, kwargs[kwarg])
            except KeyError:
                pass

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        list_of_keys = ["x", "y", "id", "size"]
        rect_dict = {}
        for key in list_of_keys:
            rect_dict[key] = getattr(self, key)
        return rect_dict
