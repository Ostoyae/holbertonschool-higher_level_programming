#!/usr/bin/python3
def uppercase(str):
    ls = list(str)
    for i in range(len(str)):
        char = ord(ls[i])
        if char >= ord('a') and char <= ord('z'):
            ls[i] = chr(char - 32)
    print("".join(ls))
