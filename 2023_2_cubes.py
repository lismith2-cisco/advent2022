### Part 1
games = {}
with open('2023_2_cubes_input.txt') as f:
  for game in f:
    game_number, reveals = game.strip().split(': ', 1)
    game_number = int(game_number.split(None, 1)[1])
    games[game_number] = {'red': 0, 'green': 0, 'blue': 0}
    for reveal in reveals.split('; '):
      for reveal_part in reveal.split(', '):
        number, colour = reveal_part.split(None, 1)
        number = int(number)
        games[game_number][colour] = max(games[game_number][colour], number)

total = 0
for game_number, results in games.items():
  if results['red'] <= 12 and results['green'] <= 13 and results['blue'] <= 14:
    total += game_number
print(total)

### Part 2
total = 0
for game_number, results in games.items():
  total += results['red'] * results['green'] * results['blue']
print(total)
