import random

lst = []

password = "password"

for letter in password:
    lst.append(letter)
print(lst)


for i in range(3):
    x = len(lst)
    pos = random.randint(0, x - 1)
    input1 = input(f"Enter letter at position {pos + 1}: ")
    if input1 == lst[pos]:
        print('Correct')
    else:
        print('Security check Failed')
        break
print('Security check passed')




