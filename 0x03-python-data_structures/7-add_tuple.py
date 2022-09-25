#!/usr/bin/python3
"""a function that adds 2 tuples."""
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0
    error = ''
    if len(tuple_a) > 1:
        a1 = tuple_a[0]
        a2 = tuple_a[1]
    else:
        try:
            a1 = tuple_a[0]
        except Exception:
            error = Exception
        try:
            a2 = tuple_a[1]
        except Exception:
            error = Exception
    if len(tuple_b) > 1:
        b1 = tuple_b[0]
        b2 = tuple_b[1]
    else:
        try:
            b1 = tuple_b[0]
        except Exception:
            error = Exception
        try:
            b2 = tuple_b[1]
        except Exception:
            error = Exception
    del error
    return (a1 + b1, a2 + b2)
