#!/usr/bin/env python3

import sys
if __name__ == '__main__':
    try:
        with open(sys.argv[1]) as f1, open(sys.argv[2]) as f2:
            file_1 = f1.read()
            file_2 = f2.read()
            if file_1 == file_2:
                print('Same')
            else:
                print('Different')
    except IndexError:
            print(f'Usage: {sys.argv[0]} <pattern> <file>')
    except FileNotFoundError:
            print(f'{sys.argv[0]}: Error opening file')