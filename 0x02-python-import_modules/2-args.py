#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv) - 1
    if n == 0:
        print("{} argument.".format(n))
    else:
        print("{} arguments:".format(n))
        for i in range(n + 1):
            if i == 0:
                continue
            print("{}: {}".format(i, sys.argv[i]))
