#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = list(my_list)
    num_to_replace = my_list.count(search)
    for i in range(0, num_to_replace):
        idx = new_list.index(search)
        new_list.remove(search)
        new_list.insert(idx, replace)
    return new_list
