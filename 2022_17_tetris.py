import itertools

tetris_pieces = itertools.cycle([
    {(0, 0), (1, 0), (2, 0), (3, 0)},
    {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},
    {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},
    {(0, 0), (0, 1), (0, 2), (0, 3)},
    {(0, 0), (1, 0), (0, 1), (1, 1)},
])

jets = itertools.cycle(open("2022_17_tetris_input.txt").read())

for tetris_piece in itertools.islice(tetris_pieces, 12):
    print(tetris_piece)

for jet in itertools.islice(jets, 12):
    print(jet)
