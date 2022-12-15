direction_vectors = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


def get_head_moves():
    with open("2022_9_rope_input.txt") as f:
        for line in f:
            direction, number = line.strip().split()
            direction_vector = direction_vectors[direction]
            for i in range(int(number)):
                yield direction_vector


def get_new_position(current_position, leading_knot_position):
    difference_x = leading_knot_position[0] - current_position[0]
    difference_y = leading_knot_position[1] - current_position[1]
    new_x = round(difference_x * 1.1 / 2) + current_position[0]
    new_y = round(difference_y * 1.1 / 2) + current_position[1]
    if new_x == leading_knot_position[0] and new_y == leading_knot_position[1]:
        return current_position
    return (new_x, new_y)


knots_position = [(0, 0)] * 10

all_tail_positions = {
    knots_position[-1]
}

for move_x, move_y in get_head_moves():
    knots_position[0] = (knots_position[0][0] + move_x,
                         knots_position[0][1] + move_y)
    for i in range(1, 10):
        knots_position[i] = get_new_position(
            knots_position[i], knots_position[i-1])
    all_tail_positions.add(knots_position[-1])

print(len(all_tail_positions))
