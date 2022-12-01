from collections import Counter
with open("2021_6_lanternfish_input.txt") as f:
    initial_fish = (int(fish) for fish in f.readline().split(','))

fish_count = Counter(initial_fish)

for day in range(256):
    new_fish_count = Counter(
        {countdown: fish_count[countdown + 1] for countdown in range(8)})
    new_fish_count[6] += fish_count[0]
    new_fish_count[8] += fish_count[0]
    fish_count = new_fish_count

print(fish_count.total())
