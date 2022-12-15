from itertools import chain


lines = ((int(char) for char in line.strip())
         for line in open("2022_8_trees_input.txt"))


class Tree:
    def __init__(self, height, x_pos, y_pos):
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __repr__(self):
        return f"Tree({self.height}, {self.x_pos}, {self.y_pos})"

    def scenic_score(self):
        return self.look_up() * self.look_down() * self.look_left() * self.look_right()

    def calculate_view(self, tree_iterator):
        view = 0
        for tree in tree_iterator:
            view += 1
            if tree.height >= self.height:
                break
        return view

    def look_up(self):
        tree_iterator = (tree_map[y_pos][self.x_pos]
                         for y_pos in reversed(range(self.y_pos)))
        return self.calculate_view(tree_iterator)

    def look_down(self):
        tree_iterator = (tree_map[y_pos][self.x_pos]
                         for y_pos in range(self.y_pos + 1, len(tree_map)))
        return self.calculate_view(tree_iterator)

    def look_left(self):
        tree_iterator = (tree_map[self.y_pos][x_pos]
                         for x_pos in reversed(range(self.x_pos)))
        return self.calculate_view(tree_iterator)

    def look_right(self):
        tree_iterator = (tree_map[self.y_pos][x_pos]
                         for x_pos in range(self.x_pos + 1, len(tree_map[self.y_pos])))
        return self.calculate_view(tree_iterator)


tree_map = [[Tree(height, x_pos, y_pos) for x_pos, height in enumerate(line)]
            for y_pos, line in enumerate(lines)]

print(max(tree.scenic_score() for tree in chain.from_iterable(tree_map)))
