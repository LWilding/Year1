#!/usr/bin/env python3

if __name__ == '__main__':

    def f_to_c(x):
        c = (x-32)*5/9
        print(f"{c}C")


temp = input("Please enter a temperature: ")
temp = (temp[:-1])
temp = int(temp)
f_to_c(temp)

