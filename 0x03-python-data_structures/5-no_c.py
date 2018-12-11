#!/usr/bin/python3
def no_c(my_string):
    str = list(my_string)

    for i, c in enumerate(str):
        if str[i] == "c" or str[i] == "C":
            str.pop(i)

    return "".join(str)
