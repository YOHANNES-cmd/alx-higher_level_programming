#!/usr/bin/python3
"""
This is module 1-my_list

This module contains one class and one public instance method

Access test for this class in /tests subfolder - to run:
`python 3 -m doctest ./tests/1-my_list.txt`
"""


class MyList(list):
    """
    inherits from `list`

    Public instance method:
    `def print_sorted(self):`

    Args:
    list

    Returns:
    prints to stdout list sorted by ascending order
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        sorted_list = MyList()
        for item in self:
            sorted_list.append(item)
        print(sorted(sorted_list))
