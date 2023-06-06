#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq_list = list(dict.fromkeys(my_list))
    return sum(uniq_list, 0)
