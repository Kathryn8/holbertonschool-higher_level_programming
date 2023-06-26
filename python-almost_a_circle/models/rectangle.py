#!/usr/bin/python3
"""Here is the module description"""
from models.base import Base


class Rectangle(Base):
    """Description of the the class Rectangle"""

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """"Validates the width value as positive integer"""
        if type(value) != int:
            raise TypeError("Value must be integer")
        if value < 0:
            raise ValueError("Value must be positive")
        self.__width = value

    @property
    def height(self):
        """Get height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Validates the height value as positive integer"""
        if type(value) != int:
            raise TypeError("Value must be intger")
        if value < 0:
            raise ValueError("Value must be positive")
        self.__height = value

    @property
    def x(self):
        """Get the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Validates the x value"""
        self.__x = value

    @property
    def y(self):
        """Get the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Validates the y value"""
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor function"""
        super(Rectangle, self).__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
