#!/usr/bin/python3

""" a function that removes all characters c and C from a string"""


def no_c(my_string):
    new_string = ''
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        new_string += char
    return new_string
