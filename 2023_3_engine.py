from uuid import uuid4

### Part 1
def get_adjacent_points(x0, y0):
  return set((x, y) for x in (x0-1, x0, x0+1) for y in (y0-1, y0, y0+1))

with open('2023_3_engine_input.txt') as f:
  current_number = ''
  current_adjacent_points = set()
  numbers = []
  symbol_points = set()
  for y, line in enumerate(f):
    for x, c in enumerate(line.strip()):
      if c.isdigit():
        current_number += c
        current_adjacent_points |= get_adjacent_points(x, y)
      else:
        if current_number:
          numbers.append((current_number, current_adjacent_points))
          current_number = ''
          current_adjacent_points = set()
        if c != '.':
          symbol_points.add((x,y))

total = 0
for number, adjacent_points in numbers:
  if not adjacent_points.isdisjoint(symbol_points):
    total += int(number)
print(total)

### Part 2
def get_adjacent_points(x0, y0):
  return ((x, y) for x in (x0-1, x0, x0+1) for y in (y0-1, y0, y0+1))

with open('2023_3_engine_input.txt') as f:
  current_number = ''
  current_number_points = []
  number_points = {}
  asterisk_points = []
  for y, line in enumerate(f):
    for x, c in enumerate(line.strip()):
      if c.isdigit():
        current_number += c
        current_number_points.append((x, y))
      else:
        if current_number:
          number_object = (int(current_number), uuid4())
          number_points |= {point: number_object for point in current_number_points}
          current_number = ''
          current_number_points = []
        if c == '*':
          asterisk_points.append((x,y))

total = 0
for asterisk_point in asterisk_points:
  adjacent_numbers = set()
  for point in get_adjacent_points(*asterisk_point):
    adjacent_number = number_points.get(point)
    if adjacent_number:
      adjacent_numbers.add(adjacent_number)
  if len(adjacent_numbers) == 2:
    total += adjacent_numbers.pop()[0] * adjacent_numbers.pop()[0]
print(total)
