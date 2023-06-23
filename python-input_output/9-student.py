#!/usr/bin/python3
"""Module that contains the functon class_to_json"""


class Student:
    """A class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Function to instantiate a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation"""
        return vars(self)
