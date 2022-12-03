lines = (set(line.strip()) for line in open("2022_3_rucksack_input.txt"))
badges = ((a & b & c).pop() for a, b, c in zip(lines, lines, lines))
print(sum(ord(badge) - (96 if badge.islower() else 38) for badge in badges))
