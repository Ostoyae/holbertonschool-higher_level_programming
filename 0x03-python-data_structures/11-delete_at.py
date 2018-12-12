#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or len(my_list) - 1 < idx:
        return my_list
    for i, ele in enumerate(my_list):
        if idx == i:
            del my_list[i]
    return my_list
