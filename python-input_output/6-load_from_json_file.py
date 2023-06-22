#!/usr/bin/python3
"""This module contains the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """reads from json file and creates python object"""
    with open(filename, 'r', encoding="utf-8") as f:
        file_data = f.read()
        new_obj = json.loads(file_data)
        return new_obj
