#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    total = 0
    for i in range(1, argc):
        total = total + int(argv[i])
    print(total)
