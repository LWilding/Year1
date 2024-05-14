#!/usr/bin/env python3

import sys
import statistics





if __name__ == '__main__':
    pass

    if len(sys.argv) > 1:
        args = sys.argv[1:]
        temps = [int(x) for x in args]


        max = max(temps)
        min = min(temps)
        mean = statistics.mean(temps)
        print(f"The maximum temperature was {max}C, the minimum was {min}C and the mean was {mean}C")
    else:
        print('No arguments provided')
