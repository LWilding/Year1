#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    arg = sys.argv[1:]
    arg_sorted = sorted(arg, key=len)
    print(arg_sorted[0])