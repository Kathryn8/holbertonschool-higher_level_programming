#!/usr/bin/python3

"""
This is a module that contains the add_integer function.
You cna import this module with:
__import__('0-add_integer').add_integer
"""


def add_integer(a, b=98):
    """add_integer function doc string

    Args:
        a: required, can be integer or float
        b: optional, can be integer or float, default value is 98

    Returns:
       The integer value of a plus b

    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    try:
        result =  int(a) + int(b)
    except NameError:
        result = 0
    return result
