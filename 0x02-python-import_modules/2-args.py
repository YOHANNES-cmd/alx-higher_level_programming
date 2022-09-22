#!/usr/bin/python3

if __name__ == "__main__":
    """This program prints the number of and the list of its arguments"""
    import sys

    argv = sys.argv
    index = 1
    counter = len(argv)-1

    if counter == 1:
        print("{} argument:".format(counter))
        print("{}: {}".format(index, argv[counter]))
    elif counter == 0:
        print("{} arguments.".format(counter))
    else:
        print("{} arguments:".format(counter))
        while index <= counter:
            print("{}: {}".format(index, argv[index]))
            index += 1
