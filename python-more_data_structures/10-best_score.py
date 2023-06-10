#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    key_list = list(a_dictionary.keys())
    values_list = list(a_dictionary.values())
    max_value = max([i for i in values_list if i is not None])
    pos = values_list.index(max_value)
    return key_list[pos]
