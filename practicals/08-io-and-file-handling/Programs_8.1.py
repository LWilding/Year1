#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    line_no = 0
    if sys.argv[1] == 'unix.txt':
        with open(sys.argv[1]) as u:
            for line in u:
                line_no += 1
                print(f'{line_no}: {line}')