from functools import total_ordering


@total_ordering
class RockPaperScissors:
    hand_shape_mapping = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
        'X': 'Rock',
        'Y': 'Paper',
        'Z': 'Scissors',
    }
    score_mapping = {
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3
    }

    def __init__(self, hand_shape):
        self.hand_shape = hand_shape
        self.score = self.score_mapping[self.hand_shape]

    def __eq__(self, other):
        return self.score == other.score

    def __gt__(self, other):
        return (self.score - other.score) % 3 == 1

    @classmethod
    def from_letter(cls, letter):
        hand_shape = cls.hand_shape_mapping[letter]
        return cls(hand_shape)


result_mapping = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

splitlines = (line.strip().split()
              for line in open("2022_2_scissors_input.txt"))

rounds = ((RockPaperScissors.from_letter(them), result_mapping[result])
          for them, result in splitlines)

rock = RockPaperScissors('Rock')
paper = RockPaperScissors('Paper')
scissors = RockPaperScissors('Scissors')

options = (rock, paper, scissors)

total_score = 0
for them, result in rounds:
    if result == 'win':
        total_score += 6
        me = next(option for option in options if option > them)
    elif result == 'draw':
        total_score += 3
        me = next(option for option in options if option == them)
    elif result == 'lose':
        total_score += 0
        me = next(option for option in options if option < them)
    total_score += me.score

print(total_score)
