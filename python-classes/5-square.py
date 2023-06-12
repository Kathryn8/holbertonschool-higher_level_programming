#!/usr/bin/python3
"""Define a class Square."""


class Square():
    """An class called Square."""

    def __init__(self, size=0):
        """Initialise a Square object with hidden size"""
        self.__size = size

    @property
    def size(self):
        """Returns the hidden size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set a new size with checks"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """A function to find the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """A function to print the square with hash symbols"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for i in range(self.__size):
                print('#', end="")
            print()
