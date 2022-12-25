from itertools import islice


def get_sprite_pixels():
    x = 1
    with open("2022_10_addx_input.txt") as f:
        for line in f:
            line = line.strip()
            if line == 'noop':
                yield (x-1, x, x+1)
            else:
                yield (x-1, x, x+1)
                yield (x-1, x, x+1)
                x += int(line.split()[1])


sprite_pixels_iterator = get_sprite_pixels()

for _ in range(6):
    output_line = ''
    for crt_pos, sprite_pixels in zip(range(40), sprite_pixels_iterator):
        if crt_pos in sprite_pixels:
            output_line += '#'
        else:
            output_line += '.'
    print(output_line)
