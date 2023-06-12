#!/usr/bin/python3
"""Define a class Square."""


class Square():
    """An class called Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise a Square object with hidden size"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Returns the hidden position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set a new position with checks"""
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """A function to find the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """A function to print the square with hash symbols"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print('#', end="")
            print()
