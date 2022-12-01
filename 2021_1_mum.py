f = open("2021_1_warmup_input.txt")

count = 0
prev = None

for line in f:
    depth = int(line)
    if prev is None:
        pass
    elif depth > prev:
        count += 1
    prev = depth

print(count)
