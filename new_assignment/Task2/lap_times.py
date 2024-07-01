#!/usr/bin/env python3

if __name__ == '__main__':
    pass

lap_times = {}

print('Grand Prix Race Times')
race_name = input('Enter name of race: ')
if not race_name:
    race_name = 'Leeds Beckett'

while True:
    lap_input = input('Enter Driver and Time [Enter to Finish]: ')
    if not lap_input:
        break
    driver_id = lap_input[:3]
    lap_speed = float(lap_input[3:])

    if driver_id not in lap_times:
        lap_times[driver_id] = []

    lap_times[driver_id].append(lap_speed)

print('\n')
print(f'Grand Prix de {race_name} Timings')
x = 22+len(race_name)
print('=' * x + '\n')
print(f'{len(lap_times)} Drivers Entered.'+'\n')
print('   Laps      Fast      Slow      Mean')

for driver, lt in lap_times.items():
    lap_no = len(lt)
    fastest_lap = min(lt)
    slowest_lap = max(lt)
    mean = sum(lt)/lap_no
    print(f'{driver}   {lap_no}   {fastest_lap}   {slowest_lap}   {mean}')
