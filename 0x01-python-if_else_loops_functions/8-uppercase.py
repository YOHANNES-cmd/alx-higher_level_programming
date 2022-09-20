#!/usr/bin/python3
def uppercase(str):
    temp = ""
    for char in str:
        if char.islower():
            temp += chr(ord(char)-32)
        else:
            temp += char
    print("{}".format(temp))
