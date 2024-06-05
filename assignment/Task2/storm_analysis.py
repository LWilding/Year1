#!/usr/bin/env python3

import sys
from statistics import mean
import os

if __name__ == '__main__':
    pass

town_speeds = {}
storm_speeds = {}
highest_ws_location = set()
location_list = ""
highest_ws = -1
worst_storm_speed = -1


try:
    if os.stat(sys.argv[1]).st_size > 0:
        print(f"Wind Speed Analysis")
        print('~~~~~~~~~~~~~~~~~~~')

        with open(sys.argv[1]) as data:
            for line in data:
                town, wind_speed, storm = line[:-1].split(',')
                wind_speed = int(wind_speed)

                if wind_speed > highest_ws:
                    highest_ws = wind_speed
                    highest_ws_location = {town}
                elif highest_ws == wind_speed:
                    highest_ws_location.add(town)

                if town in town_speeds:
                    town_speeds[town].append(wind_speed)
                else:
                    town_speeds[town] = [wind_speed, ]

                if storm in storm_speeds:
                    storm_speeds[storm].append(wind_speed)
                else:
                    storm_speeds[storm] = [wind_speed, ]

            print(f"\nHighest Speed Recorded: {highest_ws} MPH")

            for town in highest_ws_location:
                location_list += f"{town}, "

            print(f"\n{highest_ws}MPH recorded at: {location_list}\n")

            for town, wind_speed in town_speeds.items():
                average_speed = mean(wind_speed)
                print(f"{town}: Average Speed {average_speed:.2f} MPH")



            for town, wind_speed in town_speeds.items():
                if mean(wind_speed) > worst_storm_speed:
                    worst_storm_speed = mean(wind_speed)
                    worst_storm = storm
            print(f"\nWorst storm was Storm {worst_storm} with average"
                  f" gusts of {worst_storm_speed:.2f} MPH!")
    else:
        print("Empty File")
except FileNotFoundError:
    print("This File Does Not Exist")
except ValueError:
    print("Invalid File")

