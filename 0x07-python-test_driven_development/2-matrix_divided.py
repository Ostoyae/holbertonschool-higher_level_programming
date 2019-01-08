#!/usr/bin/python3

"""
Task 1 Module: Divide a Matrix

Basic functionality should alway pass at minimum
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 3) # doctest: +NORMALIZE_WHITESPACE
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
>>> matrix # doctest: +NORMALIZE_WHITESPACE
[[1, 2, 3], [4, 5, 6]]
"""


def matrix_divided(matrix, div):
    """Returns a new matrix divided by div

    all values divided by div will be rounded to the 2 decimal place
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of\
                        integers/floats")
    try:
        if not isinstance(matrix[0], list):
            raise TypeError("matrix must be a matrix (list of lists) of\
                             integers/floats")
        size = len(matrix[0])
        if size is 0:
            raise TypeError("matrix must be a matrix (list of lists) of\
                            integers/floats")
    except IndexError:
        raise TypeError("matrix must be a matrix (list of lists) of\
            integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    for row in matrix:
        if len(row) is not size:
            raise TypeError("Each row of the matrix must have the\
                            same size")
    try:
        mtx_cpy = list(map(lambda row: list(
            map(lambda ele: round(ele / div, 2), row)), matrix))
    except (ValueError, TypeError):
        raise TypeError("matrix must be a matrix (list of lists) of\
                        integers/floats")
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")
    return mtx_cpy


if __name__ == "__main__":
    import doctest
    doctest.testmod()
