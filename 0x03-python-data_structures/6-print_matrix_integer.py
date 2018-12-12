#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if type(matrix) == list:
        for pos in matrix:
            if type(pos) == list:
                lngth = len(pos)
                for i in range(lngth):
                    print(
                            "{:d}".format(pos[i]),
                            end="{}".format(
                                " " if i < lngth - 1 else "\n"))
            else:
                return None
