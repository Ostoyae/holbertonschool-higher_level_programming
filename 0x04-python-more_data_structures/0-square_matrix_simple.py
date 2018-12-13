#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cpy = matrix.copy()
    square = lambda x : x**2
    for i, d1 in enumerate(cpy):
        cpy[i] = list(map(square, d1))
    return cpy
