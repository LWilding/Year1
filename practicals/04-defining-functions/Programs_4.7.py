#!/usr/bin/env python3

import statistics

if __name__ == '__main__':


    temps = []

x = int(input("How many values would you like to enter?: "))

for i in range(x):
        temp_list = input(f"Enter temperatures #{i + 1}: ")
        temp_list = (temp_list[:-1])
        temp_list = int(temp_list)
        if 0 < temp_list:
            temps.append(temp_list)



max = max(temps)
min = min(temps)
mean = statistics.mean(temps)
print(f"The maximum temperature was :{max}C, the minimum was:{min}C and the mean was: {mean}C")