#!/usr/bin/python3
for i in range(0, 10):
    for x in range(1, 10):
        if i != x and x > i:
            if i == 8 and x == 9:
                print("{0}{1}".format(i, x))
            else:
                print("{0}{1}".format(i, x), end=', ')
