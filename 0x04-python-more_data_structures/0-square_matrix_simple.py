#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_matrix = []

    for row in matrix:
        row_squared = []
        for elem in row:
            row_squared.append(elem ** 2)
        new_matrix.append(row_squared)

    return new_matrix
