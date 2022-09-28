#!/usr/bin/python3

"""a function that returns
the number of keys in a dictionary"""


def number_keys(a_dictionary):
    keys = 0
    for key in a_dictionary.keys():
        keys += 1
    return keys


"""return len(a_dictionary.keys()) can be used
alternatively to extract the number of keys."""
