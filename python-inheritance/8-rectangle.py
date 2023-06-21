#!/usr/bin/python3
"""Module that contains the class BaseGeometry"""


class BaseGeometry:
    """A class called BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value


class Rectangle(BaseGeometry):
    """A class that defines a rectangle"""
    def __init__(self, width, height):
        """Initialise the height and width"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
