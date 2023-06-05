#!/usr/bin/python3


def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    if length == 1:
        return my_list[0]
    my_list.sort(reverse=True)
    return my_list[0]
