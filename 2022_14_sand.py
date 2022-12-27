from itertools import tee, count

occupied_points = set()
max_y = 0


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


for line in open("2022_14_sand_input.txt"):
    splitline = line.strip().split(' -> ')
    strpoints = (point.split(',') for point in splitline)
    points = ((int(x), int(y)) for x, y in strpoints)
    point_pairs = pairwise(points)
    for point_one, point_two in point_pairs:
        max_y = max(max_y, point_one[1], point_two[1])
        if point_one[0] == point_two[0]:
            occupied_points |= {(point_one[0], y) for y in range(
                min(point_one[1], point_two[1]), max(point_one[1], point_two[1]) + 1)}
        else:
            occupied_points |= {(x, point_one[1]) for x in range(
                min(point_one[0], point_two[0]), max(point_one[0], point_two[0]) + 1)}


floor_y = max_y + 2
finished = False
for unit in count(start=1):
    x, y = (500, 0)
    while True:
        for next_position in ((x, y+1), (x-1, y+1), (x+1, y+1)):
            if next_position not in occupied_points and next_position[1] < floor_y:
                x, y = next_position
                break
        else:
            occupied_points.add((x, y))
            if (x, y) == (500, 0):
                finished = True
            break
    if finished:
        break

print(unit)
