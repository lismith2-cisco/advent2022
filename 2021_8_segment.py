from collections import Counter, defaultdict

f = open("2021_8_segment_input.txt")


def parse_line(line):
    unique_pattern_text, output_value_text = line.split(" | ")
    unique_patterns = [frozenset(pattern)
                       for pattern in unique_pattern_text.split()]
    output_values = [frozenset(pattern)
                     for pattern in output_value_text.split()]
    return unique_patterns, output_values


parsed_lines = (parse_line(line) for line in f)


def get_digit_mapping(unique_patterns):
    reverse_digit_mapping = {}
    unique_sets_by_length = defaultdict(list)
    for pattern in unique_patterns:
        unique_sets_by_length[len(pattern)].append(pattern)
    reverse_digit_mapping['1'] = unique_sets_by_length[2][0]
    reverse_digit_mapping['4'] = unique_sets_by_length[4][0]
    reverse_digit_mapping['7'] = unique_sets_by_length[3][0]
    reverse_digit_mapping['8'] = unique_sets_by_length[7][0]
    for pattern in unique_sets_by_length[6]:
        if len(pattern & reverse_digit_mapping['1']) == 1:
            reverse_digit_mapping['6'] = pattern
        elif len(pattern & reverse_digit_mapping['4']) == 4:
            reverse_digit_mapping['9'] = pattern
        else:
            reverse_digit_mapping['0'] = pattern
    for pattern in unique_sets_by_length[5]:
        if len(pattern & reverse_digit_mapping['1']) == 2:
            reverse_digit_mapping['3'] = pattern
        elif len(pattern & reverse_digit_mapping['6']) == 5:
            reverse_digit_mapping['5'] = pattern
        else:
            reverse_digit_mapping['2'] = pattern
    return {pattern: digit for digit, pattern in reverse_digit_mapping.items()}


total = 0
for unique_patterns, output_values in parsed_lines:
    digit_mapping = get_digit_mapping(unique_patterns)
    real_output = int(''.join(
        digit_mapping[pattern] for pattern in output_values))
    total += real_output
print(total)
