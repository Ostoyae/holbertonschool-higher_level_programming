#!/usr/bin/python3
""" 
Task 0 Module: addition for integer/float function

>>> add_integer(10)
108
"""
def add_integer(a, b=98):
    """Return the addition for integers/float as an integer value
    
    >>> add_integer(2)
    100
    >>> add_integer(1, 1)
    2

    passing float are OK, but will be casted as an integer
    >>> add_integer(0.1)
    98
    >>> add_integer(1.5, 1.5)
    2

    passing anything other than a integer or float will raise an TypeError
    >>> add_integer("test")
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer

    >>> add_integer(10.5, "cat")
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
