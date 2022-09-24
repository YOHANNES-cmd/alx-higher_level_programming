#!/usr/bin/python3

""" a function that replaces an element in a list at a specific position
without modifying the original list (like in C)."""


def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = my_list[:]
    if idx < 0 or len(my_list) - 1 < idx:
        return new_list
    new_list[idx] = element
    return new_list
