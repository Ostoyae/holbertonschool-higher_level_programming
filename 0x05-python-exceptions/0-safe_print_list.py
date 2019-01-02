#/usr/bin/python3

def safe_print_list(mylist=[], x=0):
    i = 0
    while i < x:
        try:
            print("{}".format(mylist[i]), end="")
            i += 1 
        except IndexError:
            break
    print()
    return i
