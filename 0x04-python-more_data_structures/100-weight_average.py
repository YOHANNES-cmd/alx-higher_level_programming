#!/usr/bin/python3

"""a function that returns the weighted
average of all integers tuple"""


def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    size = 0
    for tup in my_list:
        num += (tup[0] * tup[1])
        size += tup[1]
    return (num / size)
