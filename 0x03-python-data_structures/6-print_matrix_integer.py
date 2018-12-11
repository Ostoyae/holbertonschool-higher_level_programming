#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for pos in matrix:
        lngth = len(pos)
        for i in range(lngth):
            print(
                    "{:d}".format(pos[i]),
                    end="{}".format(
                        " " if i < lngth - 1 else "\n"))
