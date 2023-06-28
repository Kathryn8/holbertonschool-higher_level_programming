#!/usr/bin/python3
"""Here is the module description"""
import json
import gc


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
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w', encoding="utf-8") as new_file:
            new_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary != {}:
            if cls.__name__ == 'Rectangle':
                dummy = cls(2, 3)
            else:
                dummy = cls(2)
        dummy.update(**dictionary)
        return dummy
