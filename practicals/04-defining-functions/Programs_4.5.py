#!/usr/bin/env python3

if __name__ == '__main__':

    def c_to_f(x):
        f = x*9/5+32
        print(f)

    def f_to_c(x):
        c = (x-32)*5/9
        print(c)


c_to_f(30)
f_to_c(86)