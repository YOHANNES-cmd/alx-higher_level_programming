#!/usr/bin/python3

"""a function that deletes keys with
a specific value in a dictionary."""


def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for key, val in a_dictionary.items():
            if val == value:
                del a_dictionary[key]
                break

    return (a_dictionary)
