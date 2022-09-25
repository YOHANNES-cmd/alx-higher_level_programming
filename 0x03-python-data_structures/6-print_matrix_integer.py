#!/usr/bin/python3

"""a function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for i in range(length):
        for j in matrix[i]:
            if j != matrix[i][len(matrix[i])-1]:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
        print("")
