from statistics import mean
with open("2021_7_whale_input.txt") as f:
    crab_positions = [int(crab_position)
                      for crab_position in f.readline().split(',')]


def calculate_single_fuel(alignment_position, position):
    distance = abs(alignment_position - position)
    return (distance * (distance + 1) // 2)


def calculate_total_fuel(alignment_position):
    return sum(calculate_single_fuel(alignment_position, position) for position in crab_positions)


best_position = None
best_fuel = None
for alignment_position in range(min(crab_positions), max(crab_positions)+1):
    fuel = calculate_total_fuel(alignment_position)
    if best_fuel is None or fuel < best_fuel:
        best_position = alignment_position
        best_fuel = fuel
print(best_position)
print(best_fuel)
