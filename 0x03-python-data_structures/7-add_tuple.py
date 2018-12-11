#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a = list(tuple_a)
    b = list(tuple_b)

    if len(a) < 1:
        a.append(0)
    if len(a) < 2:
        a.append(0)
    if len(b) < 1:
        b.append(0)
    if len(b) < 2:
        b.append(0)
    sum = []
    for i in range(2):
        sum.append(a[i] + b[i])
    return tuple(sum)
