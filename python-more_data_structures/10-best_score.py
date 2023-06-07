#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    invert_dict = {v: k for (k, v) in a_dictionary.items()}
    max_value = max(invert_dict.keys())
    return invert_dict.get(max_value)
