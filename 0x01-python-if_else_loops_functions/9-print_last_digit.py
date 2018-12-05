#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        digit = -number % 10
    else:
        digit = number % 10

    if digit == 0:
        print("0", end="")
        return 0
    else:
        print("{}".format(digit), end="")
        return digit
