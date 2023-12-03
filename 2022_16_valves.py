import re
from functools import cached_property
from math import inf
from itertools import count, permutations
from copy import deepcopy


class Valve:
    def __init__(self, name, flow_rate, connected_valves):
        self.name = name
        self.flow_rate = flow_rate
        self._connected_valves = connected_valves

    @cached_property
    def connected_valves(self):
        return [all_valves[valve] for valve in self._connected_valves]

    def __repr__(self):
        return f"Valve({self.name}, {self.flow_rate}, {self._connected_valves}"

    @cached_property
    def distances_to_working_valves(self):
        num_valves = len(all_valves)
        distances = {self.name: 0}
        current_valves = [self]
        for distance in count(start=1):
            new_valves = []
            for current_valve in current_valves:
                for connected_valve in current_valve.connected_valves:
                    if connected_valve.name in distances:
                        continue
                    distances[connected_valve.name] = distance
                    if len(distances) == num_valves:
                        break
                    new_valves.append(connected_valve)
                else:
                    continue
                break
            else:
                current_valves = new_valves
                continue
            break
        return {valve.name: distances[valve.name] for valve in working_valves}


all_valves = {}
working_valves = []

line_re = re.compile(
    r"Valve (?P<name>\w+) has flow rate=(?P<rate>\d+); tunnels? leads? to valves? (?P<valves>.+)")

start = None
for line in open("2022_16_valves_input.txt"):
    match = re.match(line_re, line)
    name = match.group('name')
    flow_rate = int(match.group('rate'))
    connected_valves = match.group('valves').split(', ')
    valve = Valve(name, flow_rate, connected_valves)
    all_valves[name] = valve
    if name == 'AA':
        start = valve
    if flow_rate > 0:
        working_valves.append(valve)


def calculate_route_pressure_release(start, route):
    route_pressure = 0
    current_valve = start
    remaining_time = 30
    for next_valve in route:
        travel_time = current_valve.distances_to_working_valves[next_valve.name]
        remaining_time -= travel_time
        valve_turn_time = 1
        remaining_time -= valve_turn_time
        if remaining_time <= 0:
            break
        valve_total_pressure = next_valve.flow_rate * remaining_time
        route_pressure += valve_total_pressure
    return route_pressure


greatest_flow_route = sorted(
    working_valves, key=lambda x: x.flow_rate, reverse=True)


def nearest_route(start):
    visited = set()
    current_valve = start
    if start in working_valves:
        visited.add(start.name)
        yield start
    while True:
        next_valve_name, distance = min(((name, distance) for (name, distance) in current_valve.distances_to_working_valves.items(
        ) if name not in visited), default=(None, None), key=lambda x: x[1])
        if next_valve_name is None:
            return
        visited.add(next_valve_name)
        current_valve = all_valves[next_valve_name]
        yield current_valve


greatest_flow_pressure = calculate_route_pressure_release(
    start, greatest_flow_route)
nearest_route_pressure = calculate_route_pressure_release(
    start, nearest_route(start))
best_pressure = 0  # max(greatest_flow_pressure, nearest_route_pressure)


def calculate_best_route(valve, route):
    global best_pressure
    # get the next valve options
    next_valve_options = [(name, distance) for (name, distance)
                          in valve.distances_to_working_valves.items() if name not in route['visited']]
    if not next_valve_options:
        if route['route_pressure'] > best_pressure:
            best_pressure = route['route_pressure']
            print(route['visited_list'])
        return
    for name, distance in next_valve_options:
        next_route = deepcopy(route)
        next_valve = all_valves[name]
        # travel there
        next_route['remaining_time'] -= distance
        # turn the valve
        next_route['remaining_time'] -= 1
        if next_route['remaining_time'] <= 0:
            if next_route['route_pressure'] > best_pressure:
                best_pressure = next_route['route_pressure']
                print(next_route['visited_list'])
            return
        next_route['route_pressure'] += next_valve.flow_rate * \
            next_route['remaining_time']
        next_route['visited'].add(next_valve.name)
        next_route['visited_list'].append(next_valve.name)
        next_route['visited_list'].append(
            next_valve.flow_rate * next_route['remaining_time'])
        # calculate the next step
        calculate_best_route(next_valve, next_route)


initial_route = {
    'visited': set(),
    'visited_list': [],
    'route_pressure': 0,
    'remaining_time': 30
}

calculate_best_route(start, initial_route)

print(best_pressure)
