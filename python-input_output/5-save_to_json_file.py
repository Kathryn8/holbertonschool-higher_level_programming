#!/usr/bin/python3
"""This module contains the save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes python object to text file in json format"""
    json_str = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf=8") as open_file:
        num_char = open_file.write(json_str)
