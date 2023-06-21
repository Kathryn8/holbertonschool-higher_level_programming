#!/usr/bin/python3
"""Module that contains the class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle"""
    def __init__(self, width, height):
        """Initialise the height and width"""
        self.__width = BaseGeometry().integer_validator("width", width)
        self.__height = BaseGeometry().integer_validator("height", height)
