f = open("2021_4_squid_input.txt")


class Board:
    def __init__(self, rows):
        self.unmarked_row_sets = [set(row) for row in rows]
        self.unmarked_column_sets = [set(column_tuple)
                                     for column_tuple in zip(*rows)]
        self.num_balls_added = 0

    def add_ball(self, ball):
        self.num_balls_added += 1
        bingo = False
        for line in self.unmarked_row_sets + self.unmarked_column_sets:
            line.discard(ball)
            if not line:
                bingo = True
        return bingo

    def get_total_unmarked_numbers(self):
        return sum(sum(int(num) for num in unmarked_row_set) for unmarked_row_set in self.unmarked_row_sets)


lines = (line.strip() for line in f)
balls = next(lines).split(',')
print(balls)
current_rows = []
worst_board = None

for line in lines:
    print(line)
    if line:
        current_rows.append(line.split())
    else:
        if not current_rows:
            continue
        current_board = Board(current_rows)
        for ball in balls:
            bingo = current_board.add_ball(ball)
            if bingo:
                break
        if worst_board is None or current_board.num_balls_added > worst_board.num_balls_added:
            worst_board = current_board
        current_rows = []

print(worst_board.get_total_unmarked_numbers())
print(int(balls[worst_board.num_balls_added - 1]))

print(worst_board.get_total_unmarked_numbers() *
      int(balls[worst_board.num_balls_added - 1]))
