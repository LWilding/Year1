import random

lst = []

password = "password"

for letter in password:
    lst.append(letter)
print(lst)

x = len(lst)
pos = random.randint(0, x-1)
pos2 = random.randint(0, x-1)
pos3 = random.randint(0, x-1)


input1 = input(f"Enter letter at position {pos + 1}: ")
if input1 == lst[pos]:
    print('Correct')

else:
    print('Failed')

input2 = input(f"Enter letter at position {pos2 + 1}: ")
if input2 == lst[pos2]:
    print('c')
else:
    print('f')

input3 = input(f"Enter letter at position {pos3 + 1}: ")
if input2 == lst[pos3]:
    print('c')
else:
    print('f')
