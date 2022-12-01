f = open("2021_2_pilot_input.txt")
state = {
    'horizontal': 0,
    'depth': 0,
    'aim': 0,
}

splitlines = (line.split() for line in f)
commands = ((direction, int(distance)) for direction, distance in splitlines)
for direction, distance in commands:
    if direction == 'up':
        state['aim'] -= distance
    elif direction == 'down':
        state['aim'] += distance
    elif direction == 'forward':
        state['horizontal'] += distance
        state['depth'] += distance * state['aim']

print(state['horizontal'] * state['depth'])
