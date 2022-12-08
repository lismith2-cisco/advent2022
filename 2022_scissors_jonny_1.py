class Play:

    @classmethod
    def create(cls, key):
        # Can we do something here to dynamically change the type at runtime?
        return Play.source_keys[key]()

    def wins(self, other):
        if isinstance(other, self.beats):
            return True
        return False


class Rock(Play):
    pass


class Paper(Play):
    pass


class Scissors(Play):
    pass


Rock.beats = Scissors
Rock.score = 1
Paper.beats = Rock
Paper.score = 2
Scissors.beats = Paper
Scissors.score = 3

Play.source_keys = {
    'X': Rock,
    'A': Rock,
    'Y': Paper,
    'B': Paper,
    'Z': Scissors,
    'C': Scissors
}


def get_winner(me, opponent) -> int:
    if me.wins(opponent):
        return 6
    elif opponent.wins(me):
        return 0
    return 3


def play(me, opponent) -> int:
    return me.score + get_winner(me, opponent)


score = 0

with open('2022_2_scissors_input.txt') as fh:
    line = fh.readline()
    while line:
        plays = line.strip().split(' ')
        score += play(Play.create(plays[1]), Play.create(plays[0]))

        line = fh.readline()

print(score)
