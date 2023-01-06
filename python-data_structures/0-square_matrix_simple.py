#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        mat = []
    for row in matrix:
        sub_matrix = map(lambda num: num**2, row)
        mat.append(list(sub_matrix))
    return mat
