f = open("2021_9_smoke_input.txt")
map = [[10] + [int(c) for c in line.strip()] + [10] for line in f]

line_length = len(map[0])

map = [[10]*line_length] + map + [[10]*line_length]

map_length = len(map)

total_risk = 0

for line_no in range(1, map_length - 1):
    for column_no in range(1, line_length - 1):
        height = map[line_no][column_no]
        if height < min(
            map[line_no][column_no + 1],
            map[line_no][column_no - 1],
            map[line_no + 1][column_no],
            map[line_no - 1][column_no],
        ):
            total_risk += height + 1
print(total_risk)
