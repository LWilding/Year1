#!/usr/bin/env python3

if __name__ == '__main__':




    def prime(x):
        for divisor in range(2,x):
            if (x % divisor) == 0:
                print(f"It's not a prime :(")
                break
        else:
            print(f"It's a prime!!!")



    prime(27)