#!/usr/bin/python3
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{alpha}".format(alpha=chr(i)), end='')
