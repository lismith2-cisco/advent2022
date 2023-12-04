### Part 1
total_points = 0
with open('2023_4_scratchcards_input.txt') as f:
  for card in f:
    winning_numbers, my_numbers = card.strip().split(': ',1 )[1].split(' | ', 1)
    number_of_winning_numbers = len(set(winning_numbers.strip().split()) & set(my_numbers.strip().split()))
    if number_of_winning_numbers:
      total_points += 2**(number_of_winning_numbers-1)
print(total_points)

### Part 2
cards = {}
total_cards = 0
with open('2023_4_scratchcards_input.txt') as f:
  for card in f:
    card_number, all_numbers = card.strip().split(': ',1 )
    card_number = int(card_number.strip('Card '))
    number_of_copies = cards.get(card_number, 0) + 1

    winning_numbers, my_numbers = all_numbers.split(' | ', 1)
    number_of_winning_numbers = len(set(winning_numbers.strip().split()) & set(my_numbers.strip().split()))

    for future_card in range(card_number + 1, card_number + 1 + number_of_winning_numbers):
      cards.setdefault(future_card, 0)
      cards[future_card] += number_of_copies
    
    total_cards += number_of_copies

print(total_cards)