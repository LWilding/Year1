#!/usr/bin/env python3

age = 1

if age >=18 and age <=30:
    print("you are still young!")

if age > 100:
    print("you are very old,")
    print("well done!")
elif age > 80:
    print("you are fairly old")
    print("pretty good!")
elif age > 40:
    print("you are middle aged")
    print("never mind")
elif age >=30 and age<40:
    print("between 30 and 40, whoooo!")
else:
    print("you are not very old - yet")


name = input("Enter your name: ")
if name == "Luke":
    print("Great name!")
if name:
    print("Your name is", name)
else:
    print("Name not entered")