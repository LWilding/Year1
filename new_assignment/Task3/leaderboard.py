#!/usr/bin/env python3

import sys
from statistics import mean
import os

if __name__ == '__main__':
    pass

driver_times = {}
lap_times = {}
driver_dict = {}

try:
    if os.stat(sys.argv[1]).st_size > 0:
        print(f'Grand Prix Practice Times')
        print('=' * 25)

        with open(sys.argv[1]) as data:
            for line in data:
                name, team, lap_time = line[:-1].split(',')
                lap_time = float(lap_time)
                if name not in lap_times:
                    lap_times[name] = []








    else:
        print("Empty File")
except FileNotFoundError:
    print("This File Does Not Exist")
except ValueError:
    print("Invalid File")


class Driver(object):
    all = []
    def __init__(self, name, team, lap_times):
        self.name = name
        self.team = team
        self.lap_times = lap_times

        Driver.all.append(self)

        data_lst = list(data)

        for line in data:
            {line+1} = Driver(name, team, lap_time = line[:-1].split(','))

print(Driver.all)