#!/usr/bin/env python3

if __name__ == '__main__':

    def encrypt():
        x = input("Enter Message Here: ")
        x = x.replace(" ","")
        x = "".join(reversed(x))
        print(x)

    encrypt()