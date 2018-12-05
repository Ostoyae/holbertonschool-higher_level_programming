#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lnth = len(sys.argv) - 1
    print(
            "{} arguments".format(lnth),
            end="{}".format(".\n") if not lnth else ":\n")
    if lnth > 0:
        for idx, item in enumerate(sys.argv):
            if idx != 0:
                print("{}: {}".format(idx, item))
