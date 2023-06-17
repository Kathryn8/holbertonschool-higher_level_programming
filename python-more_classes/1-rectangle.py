#!/usr/bin/python3

"""
Description of the module called 0-rectangle
"""


class Rectangle:
    """
    Description of the class Rectangle
    """
    def __init__(self, width=0, height=0):
        """Description of instantiation function"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """Instance method that returns the private instance variable width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Instance method that sets the private instance variable width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.___height = value

    @property
    def width(self):
        """Instance method that returns the private instance variable width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Instance method that sets the private instance variable width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
