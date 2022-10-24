#!/usr/bin/python3
"""The mylist module"""


class MyList(list):
    """My list class"""
    def print_sorted(self):
        i = self.copy()
        i.sort()
        print(i)
