#!/usr/bin/python3
"""Here is the module description"""
from models.base import Base


class Rectangle(Base):
    """Description of the the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor function"""
        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """"Sets the width value with validation"""
        self.__width = type(self).dimension_validator(self, "width", value)

    @property
    def height(self):
        """Get height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """"Sets the height value with validation"""
        self.__height = type(self).dimension_validator(self, "height", value)

    @property
    def x(self):
        """Get the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Validates the x value"""
        self.__x = type(self).coordinate_validator(self, "x", value)

    @property
    def y(self):
        """Get the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Validates the y value"""
        self.__y = type(self).coordinate_validator(self, "y", value)

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
