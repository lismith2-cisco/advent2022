from itertools import dropwhile, chain
lines = (line.strip() for line in open("2022_8_trees_input.txt"))

visible_from_top = []
visible_from_bottom = []
visible_from_right = []
visible_from_left = []

for y_pos, line in enumerate(lines):
    for x_pos, char in enumerate(line):
        height = int(char)
        if y_pos == 0:
            visible_from_top.append([(x_pos, y_pos, height)])
            visible_from_bottom.append([(x_pos, y_pos, height)])
        if x_pos == 0:
            visible_from_left.append([(x_pos, y_pos, height)])
            visible_from_right.append([(x_pos, y_pos, height)])
        if height > visible_from_top[x_pos][-1][2]:
            visible_from_top[x_pos].append((x_pos, y_pos, height))
        if height > visible_from_left[y_pos][-1][2]:
            visible_from_left[y_pos].append((x_pos, y_pos, height))
        visible_from_bottom[x_pos] = [
            (x_pos, y_pos, height)] + list(dropwhile(lambda x: x[2] <= height, visible_from_bottom[x_pos]))
        visible_from_right[y_pos] = [
            (x_pos, y_pos, height)] + list(dropwhile(lambda x: x[2] <= height, visible_from_right[y_pos]))

all_visible = set(chain.from_iterable(visible_from_top + visible_from_bottom +
                  visible_from_right + visible_from_left))
print(len(all_visible))
