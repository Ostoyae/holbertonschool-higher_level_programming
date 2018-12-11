#!/usr/bin/python3
def fizzbuzz():
    t = 100
    for i in range(1, t + 1):
        if i % 3 != 0 and i % 5 != 0:
            print("{:d}".format(i), end=" ")
            continue
        if i % 3 == 0:
            print("Fizz", end="")
        if i % 5 == 0:
            print("Buzz", end="")
        print(" ", end="")
