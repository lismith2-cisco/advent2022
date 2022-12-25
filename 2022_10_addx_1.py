from itertools import islice


def get_x():
    x = 1
    with open("2022_10_addx_input.txt") as f:
        for line in f:
            line = line.strip()
            if line == 'noop':
                yield x
            else:
                yield x
                yield x
                x += int(line.split()[1])


print(sum(cycle * x for cycle, x in islice(enumerate(get_x(), 1), 19, None, 40)))
