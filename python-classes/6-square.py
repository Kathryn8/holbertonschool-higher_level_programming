#!/usr/bin/python3
"""Define a class Square."""


class Square():
    """An class called Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise a Square object with hidden size"""
        self.size = size
        self.position = position

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
        error_msg = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(error_msg)
        if len(value) != 2:
            raise TypeError(error_msg)
        for num in value:
            if type(num) is not int:
                raise TypeError(error_msg)
            if num < 0:
                raise TypeError(error_msg)
        self.__position = value

    def area(self):
        """A function to find the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """A function to print the square with hash symbols"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print('#' * self.__size, end="")
                print()
