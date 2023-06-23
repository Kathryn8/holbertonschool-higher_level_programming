#!/usr/bin/python3
"""Module that contains the functon class_to_json"""


class Student:
    """A class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Function to instantiate a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation"""
        d = vars(self)
        if (type(attrs) == list) and ((type(x) == str) for x in attrs):
            d = {k: v for (k, v) in d.items() if k in attrs}
        return d

    def reload_from_json(self, json):
        """Replaces all attributes of the student instance"""
        self.first_name = json.get('first_name')
        self.last_name = json.get('last_name')
        self.age = json.get('age')
