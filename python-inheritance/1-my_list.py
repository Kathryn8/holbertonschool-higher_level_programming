#!/usr/bin/python3
"""A module that contains the MyList class definition"""


class MyList(list):
    """A class that inherits from the list datatype"""

    def print_sorted(self):
        """A function that sorts the list in ascending order"""
        return_list = []
        list_clone = self[:]
        for elem in range(len(list_clone)):
            min_value = min(list_clone)
            return_list.append(min_value)
            list_clone.remove(min_value)
        print(return_list)
