#!/usr/bin/python3

"""A module that contains the lookup function"""


def lookup(obj):
    """
    A function that returns the list of available attributes
    and methods of an object
    """
    return list(dir(obj))
