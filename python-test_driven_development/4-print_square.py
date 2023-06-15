#!/usr/bin/python3

"""
Module description"
"""


def print_square(size):
    """
    Description of print_square function
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
