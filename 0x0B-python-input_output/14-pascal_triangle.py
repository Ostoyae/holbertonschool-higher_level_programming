#!/usr/bin/python3

def pascal_triangle(n):
    """Create a list of lists that represents pascal's
    triangle
    """
    ls = [[1]]

    for i in range(n):
        a = ls[i]
        pascal = [1]
        for ele in range(len(a)):
            try:
                pascal.append(ls[i][ele]+ ls[i][ele+1])
            except:
                pascal.append(1)
                break
        ls.append(pascal)
    return ls

