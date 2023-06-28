#!/usr/bin/python3
"""Here is the module description"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
