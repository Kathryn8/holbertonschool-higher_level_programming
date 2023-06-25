#!/usr/bin/python3
"""Here is the module description"""


class Base:
    """Description of the the class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor function"""
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
