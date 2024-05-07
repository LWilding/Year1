#!/usr/bin/env python3

if __name__ == '__main__':


    def letter_types(s):
        return len([c for c in s if c.islower()]), len([c for c in s if c.isupper()])

print(letter_types('Wook'))

