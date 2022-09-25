#!/usr/bin/python3

"""a function that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    if my_list == []:
        return None
    my_list = sorted(my_list)
    return my_list[-1]
