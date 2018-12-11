#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    lnth = len(sys.argv) - 1
    if lnth != 3:
        sys.exit(1)
    ls = sys.argv
    a = int(ls[1])
    b = int(ls[3])
    op = ls[2]
    if op is '+':
        print("{} + {} = {}".format(a, b, cal.add(a, b)))
    elif op is '-':
        print("{} - {} = {}".format(a, b, cal.sub(a, b)))
    elif op is "*":
        print("{} * {} = {}".format(a, b, cal.mul(a, b)))
    elif op is '/':
        print("{} / {} = {}".format(a, b, cal.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
