#!/usr/bin/python3

""" a function that retrieves an element in a list like C"""


def element_at(my_list, idx):
    if idx < 0 or len(my_list) - 1 < idx:
        return None
    return my_list[idx]
