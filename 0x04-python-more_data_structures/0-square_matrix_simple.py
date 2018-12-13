#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cpy = matrix.copy()
    for i, d1 in enumerate(cpy):
        cpy[i] = list(map(lambda x: x**2, d1))
    return cpy
