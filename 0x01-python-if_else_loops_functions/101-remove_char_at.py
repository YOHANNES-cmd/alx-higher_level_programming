#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > (len(str)-1):
        return str
    else:
        copy = ""
        for x in str:
            if x == str[n]:
                continue
            else:
                copy += x
    return copy
