#!/usr/bin/python3
"""Module that contains the class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle"""
    def __init__(self, width, height):
        """Initialise the height and width"""
        self.__width = BaseGeometry().integer_validator("width", width)
        self.__height = BaseGeometry().integer_validator("height", height)

    def area(self):
        """A function that calculates the area"""
        return self.__width * self.__height

    def __str__(self):
        """Format a string for printing"""
        return f"[Rectangle] {self.__width}/{self.__height}"
