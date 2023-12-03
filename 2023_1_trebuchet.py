import re

### Part 1
with open("2023_1_trebuchet_input.txt") as f:
  lines = (line.strip() for line in f)
  total = 0
  for line in lines:
    first_digit = next(c for c in line if c.isdigit())
    last_digit = next(c for c in reversed(line) if c.isdigit())
    total += int(first_digit+last_digit)
print(total)

### Part 2
forward_match_dict = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
  'zero': '0'
}
forward_match_string = '(?:'+'|'.join([r'\d']+list(forward_match_dict.keys()))+')'
forward_match_pattern = re.compile(forward_match_string)
backward_match_dict = {k[::-1]: v for k, v in forward_match_dict.items()}
backward_match_string = '(?:'+'|'.join([r'\d']+list(backward_match_dict.keys()))+')'
backward_match_pattern = re.compile(backward_match_string)

with open("2023_1_trebuchet_input.txt") as f:
  lines = (line.strip() for line in f)
  total = 0
  for line in lines:
    first_number = re.search(forward_match_pattern, line)[0]
    first_digit = forward_match_dict.get(first_number, first_number)
    last_number = re.search(backward_match_pattern, line[::-1])[0]
    last_digit = backward_match_dict.get(last_number, last_number)
    total += int(first_digit+last_digit)
print(total)