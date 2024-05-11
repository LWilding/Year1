#!/usr/bin/env python3

if __name__ == '__main__':

    while True:
        x = int(input('Enter a number between 0-12: '))
        if 0 <= x <= 12:
            for n in range(1, 13):
                print(n, 'x', x, '=', x * n)
            break
