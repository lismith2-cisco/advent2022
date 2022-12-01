import heapq
lines = (line.strip() for line in open("2022_1_calories_input.txt"))


def get_elf_calories(lines):
    current_elf = 0
    for line in lines:
        if line:
            current_elf += int(line)
        else:
            yield current_elf
            current_elf = 0


print(sum(heapq.nlargest(3, get_elf_calories(lines))))
