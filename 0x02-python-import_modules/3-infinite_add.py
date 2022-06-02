#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    result = 0
    for i in range(n):
        if i == 0:
            continue
        result += int(sys.argv[i])
print(result)
