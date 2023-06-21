#!/usr/bin/python3
"""Module that contains the class Square"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """A class that defines a square"""
    def __init__(self, size):
        """Initialise the size"""
        self.__size = BaseGeometry().integer_validator("size", size)

    def area(self):
        """A function that calculates the area"""
        return self.__size ** 2

    def __str__(self):
        """Format a string for printing"""
        return f"[Rectangle] {self.__size}/{self.__size}"
