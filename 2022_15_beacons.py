import re
import math

line_re = re.compile(
    r"Sensor at x=(?P<sensor_x>[\d-]+), y=(?P<sensor_y>[\d-]+): closest beacon is at x=(?P<beacon_x>[\d-]+), y=(?P<beacon_y>[\d-]+)")


global_min_x = 0
global_max_x = 4000000
global_min_y = 0
global_max_y = 4000000


class Sensor:
    def __init__(self, sensor_pos, beacon_pos):
        self.sensor_pos = sensor_pos
        self.beacon_distance = abs(
            sensor_pos[0] - beacon_pos[0]) + abs(sensor_pos[1] - beacon_pos[1])

    def get_x_range(self, y):
        max_x_distance = self.beacon_distance - abs(y-self.sensor_pos[1])
        min_x = self.sensor_pos[0] - max_x_distance
        max_x = self.sensor_pos[0] + max_x_distance
        return min_x, max_x


all_sensors = []

for line in open("2022_15_beacons_input.txt"):
    match = re.match(line_re, line)
    sensor_pos = (int(match.group('sensor_x')), int(match.group('sensor_y')))
    beacon_pos = (int(match.group('beacon_x')), int(match.group('beacon_y')))
    sensor = Sensor(sensor_pos, beacon_pos)
    all_sensors.append(sensor)

for y in range(global_min_y, global_max_y + 1):
    ranges = sorted(sensor.get_x_range(y) for sensor in all_sensors)
    x = global_min_x
    for min_x, max_x in ranges:
        if min_x <= x <= max_x:
            x = max_x + 1
    if x <= global_max_x:
        break

location = (x, y)

print(location)
tuning_frequency = location[0] * 4000000 + location[1]
print(tuning_frequency)
