#!/usr/bin/python3


"""Define a class Square."""


class Square():
    """An class called Square."""
    def __init__(self, size=0):
        """Initialise a Square object with hidden size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
