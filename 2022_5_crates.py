import re
lines = (line.strip() for line in open("2022_5_crates_input.txt"))

stacks = [None, [], [], [], [], [], [], [], [], []]
for line in lines:
    if line == "1   2   3   4   5   6   7   8   9":
        break
    for stack_number in range(1, 10):
        char = line[4 * stack_number - 3]
        if char != ' ':
            stacks[stack_number].append(char)
for stack in stacks[1:]:
    stack.reverse()
next(lines)
instruction_pattern = re.compile(
    "move (?P<number>\d+) from (?P<from>\d+) to (?P<to>\d+)")

for line in lines:
    match = instruction_pattern.match(line)
    number = int(match.group('number'))
    to_stack = stacks[int(match.group('to'))]
    from_stack = stacks[int(match.group('from'))]

    to_stack.extend(from_stack[-number:])
    del from_stack[-number:]

print(''.join(stack[-1] for stack in stacks[1:]))
