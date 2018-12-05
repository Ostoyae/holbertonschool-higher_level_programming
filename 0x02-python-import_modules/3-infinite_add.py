#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    lnth = len(sys.argv) - 1
    if not lnth:
        print("0")
    else:
        for idx, i in enumerate(sys.argv):
            if idx != 0:
                sum += int(i)
    if sum:
        print(sum)
