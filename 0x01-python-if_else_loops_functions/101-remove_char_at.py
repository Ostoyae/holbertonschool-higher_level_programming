#!/usr/bin/python3
def remove_char_at(str, n):
    if len(str) < n:
        print(str)
        return
    ls = []
    for i, c in enumerate(str):
        if i != n:
            ls.append(c)
    return "".join(ls)
