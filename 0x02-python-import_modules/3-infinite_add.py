#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lnth = len(sys.argv) - 1
    if not lnth:
        print("0")
    else:
        for i in sys.argv:
            sum += int(i, 10)
    if sum:
        print(sum)
