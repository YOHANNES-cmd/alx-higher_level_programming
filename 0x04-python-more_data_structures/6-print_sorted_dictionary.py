#!/usr/bin/python3

"""a function that prints a
dictionary by ordered keys"""


def print_sorted_dictionary(a_dictionary):
    for key in sorted(list(a_dictionary.keys())):
        print(f"{key}: {a_dictionary.get(key)}")
