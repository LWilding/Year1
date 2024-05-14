#!/usr/bin/env python3

if __name__ == '__main__':

    def factors(x):
        for i in range(1, x + 1):
            if(x % i == 0):
                print(i)

factors(10)
