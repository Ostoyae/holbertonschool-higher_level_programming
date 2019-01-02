#!/usr/bin/python3
def safe_print_list_integers(mylist=[], x=0):
    i = 0
    ok = 0
    while i < x:
        try:
            print("{:d}".format(mylist[i]), end="")
        except (ValueError, TypeError):
            i += 1
            continue
        i += 1
        ok += 1
    print()
    return ok
