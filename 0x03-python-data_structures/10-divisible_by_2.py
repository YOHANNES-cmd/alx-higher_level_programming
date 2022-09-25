#!/usr/bin/python3

"""a function that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    new_list = []
    for x in my_list:
        if (x % 2):
            new_list.append(False)
        else:
            new_list.append(True)
    return new_list
