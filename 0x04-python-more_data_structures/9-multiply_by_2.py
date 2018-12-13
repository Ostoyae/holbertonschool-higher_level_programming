#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy = a_dictionary.copy()    
    for k, v in cpy.items():
            cpy[k] = v*2

    return cpy
