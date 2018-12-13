#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    rome = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000}
    ls = list(roman_string)
    s = set(roman_string)
    num = 0

    for n in ls:
        if n in list(rome):
            if num < 4000:
                num += rome.get(n)
            else:
                return 0
        else:
            continue

    return num
