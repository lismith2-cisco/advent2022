f = open("2021_1_warmup_input.txt")
numbers = [int(line) for line in f]

larger_count = 0
prev = None

for three_elements in zip(numbers, numbers[1:], numbers[2:]):
    three_total = sum(list(three_elements))
    if prev is not None:
        if prev < three_total:
            larger_count += 1
    prev = three_total

print(larger_count)
