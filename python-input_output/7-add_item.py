#!/usr/bin/python3
"""script that adds arguments to a Python list, and then save them to a file"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
list_of_args = [x for x in sys.argv if x != sys.argv[0]]
try:
    existing_object = load_from_json_file(filename)
    list_of_args = existing_object + list_of_args
except FileNotFoundError:
    pass
save_to_json_file(list_of_args, filename)
