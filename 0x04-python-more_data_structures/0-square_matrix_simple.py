#!/usr/bin/python3

""" a function that computes the
square value of all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    new_mat = [x[:] for x in matrix]
    for i in range(len(new_mat)):
        for j in range(len(new_mat[i])):
            new_mat[i][j] *= new_mat[i][j]
    return new_mat
