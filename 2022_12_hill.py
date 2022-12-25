import itertools

lines = ((ord(char) for char in line.strip())
         for line in open("2022_12_hill_input.txt"))
start = None
end = None


class Position:
    def __init__(self, height):
        global start, end
        if height == ord('S'):
            start = self
            self.height = ord('a')
        elif height == ord('E'):
            end = self
            self.height = ord('z')
        else:
            self.height = height
        self.movable_neighbours = []
        self.number_of_steps = None

    def add_neighbour(self, neighbour):
        if neighbour.height <= self.height + 1:
            self.movable_neighbours.append(neighbour)


heightmap = [[Position(height) for height in line]
             for line in lines]

for ypos, line in enumerate(heightmap):
    for xpos, position in enumerate(line):
        if ypos > 0:
            position.add_neighbour(heightmap[ypos-1][xpos])
        if ypos < len(heightmap) - 1:
            position.add_neighbour(heightmap[ypos+1][xpos])
        if xpos > 0:
            position.add_neighbour(heightmap[ypos][xpos-1])
        if xpos < len(line) - 1:
            position.add_neighbour(heightmap[ypos][xpos+1])

current_positions = [
    position for line in heightmap for position in line if position.height == ord('a')]
for position in current_positions:
    position.number_of_steps = 0
for steps in itertools.count(start=1):
    new_positions = []
    for current_position in current_positions:
        for neighbour in current_position.movable_neighbours:
            if neighbour.number_of_steps is not None:
                continue
            neighbour.number_of_steps = steps
            if neighbour is end:
                break
            new_positions.append(neighbour)
        else:
            continue
        break
    else:
        current_positions = new_positions
        continue
    break
print(end.number_of_steps)
