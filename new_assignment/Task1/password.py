#!/usr/bin/env python3
import random
if __name__ == '__main__':
    pass
lst = []

while True:
    password = input('Enter your password: ')
    if 8 < len(password):
        break
    else:
        print('Password too short.')

for letter in password:
    lst.append(letter)

for i in range(3):
    x = len(lst)
    pos = random.randint(0, x - 1)
    input1 = input(f"Enter letter at position {pos + 1}: ")
    if input1 == lst[pos]:
        print('Correct')
    else:
        print('Security check failed')
        break
else:
    print('Security check passed.')
