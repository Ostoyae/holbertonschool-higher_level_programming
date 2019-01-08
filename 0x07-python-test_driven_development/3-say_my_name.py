#!/usr/bin/python3
"""Module to print my name
"""


def say_my_name(first_name, last_name=""):
    """Function to say my name
       If first_name or last_name not string TypeError is raised
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
