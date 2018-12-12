#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ls_r = []

    for i in my_list:
        if i % 2 == 0:
            ls_r.append(True)
        else:
            ls_r.append(False)

    return ls_r
