#!/usr/bin/python3

"""a function that adds all unique integers in a
list (only once for each integer)"""


def uniq_add(my_list=[]):
    empty = []
    total = 0
    for x in my_list:
        if x not in empty:
            empty.append(int(x))
            total += x
    return total
