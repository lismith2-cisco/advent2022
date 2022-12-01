from collections import Counter

f = open("2021_3_diagnostics_input.txt")
numbers_list = [line.strip() for line in f]
line_length = len(numbers_list[0])

oxygen_numbers_list = numbers_list.copy()
for position in range(line_length):
    position_counter = Counter(numbers[position]
                               for numbers in oxygen_numbers_list)
    most_common = '1' if position_counter['1'] >= position_counter['0'] else '0'
    oxygen_numbers_list = [
        numbers for numbers in oxygen_numbers_list if numbers[position] == most_common]
    if len(oxygen_numbers_list) == 1:
        break

oxygen_generator_rating = int(oxygen_numbers_list[0], base=2)

co2_numbers_list = numbers_list.copy()
for position in range(line_length):
    position_counter = Counter(numbers[position]
                               for numbers in co2_numbers_list)
    least_common = '1' if position_counter['1'] < position_counter['0'] else '0'
    co2_numbers_list = [
        numbers for numbers in co2_numbers_list if numbers[position] == least_common]
    if len(co2_numbers_list) == 1:
        break

co2_scrubber_rating = int(co2_numbers_list[0], base=2)

print(oxygen_generator_rating * co2_scrubber_rating)
