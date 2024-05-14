#!/usr/bin/env python3

import sys
if __name__ == '__main__':
    try:
        line_no = 0
        pattern = sys.argv[2]
        with open(sys.argv[1]) as infile:
            for line in infile:
                line_no += 1
                if pattern in line:
                    print(line, line_no)
    except IndexError:
        print(f'Usage: {sys.argv[0]} <pattern> <file>')
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Error opening file')