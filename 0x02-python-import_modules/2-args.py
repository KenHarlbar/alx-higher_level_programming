#!/usr/bin/python3
import sys
n = len(sys.argv) - 1
if n == 0:
    print(f"{n} argument.")
else:
    print(f"{n} arguments:")
    for i in range(n + 1):
        if i == 0:
            continue
        print(f"{i}: {sys.argv[i]}")
