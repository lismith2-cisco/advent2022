import operator
import heapq
import math


class Monkey:
    def __init__(self, starting_items, operation, test_value, true_monkey, false_monkey):
        self.items = starting_items
        self.operation = operation
        self.test_value = test_value
        self.test = make_test(test_value)
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspection_count = 0

    def take_turn(self):
        for item in self.items:
            self.inspection_count += 1
            item = self.operation(item)
            item %= mod
            if self.test(item):
                monkeys[self.true_monkey].items.append(item)
            else:
                monkeys[self.false_monkey].items.append(item)
        self.items.clear()


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def make_operation(left, symbol, right):
    operator_function = operators[symbol]
    left = None if left == 'old' else int(left)
    right = None if right == 'old' else int(right)

    def operation(old):
        return operator_function(old if left is None else left, old if right is None else right)
    return operation


def make_test(test_value):
    def test(value):
        return not value % test_value
    return test


monkeys = []

lines = (line.strip() for line in open("2022_11_monkeys_input.txt"))

for line in lines:
    if not line:
        continue
    line = next(lines)
    starting_items = [int(item)
                      for item in line.split("Starting items: ", 1)[1].split(', ')]
    line = next(lines)
    operation = make_operation(*line.split("Operation: new = ", 1)[1].split())
    line = next(lines)
    test_value = int(line.split("Test: divisible by ", 1)[1])
    line = next(lines)
    true_monkey = int(line.split("If true: throw to monkey ", 1)[1])
    line = next(lines)
    false_monkey = int(line.split("If false: throw to monkey ", 1)[1])
    monkeys.append(Monkey(starting_items, operation,
                   test_value, true_monkey, false_monkey))

mod = math.prod(monkey.test_value for monkey in monkeys)

for _ in range(10000):
    for monkey in monkeys:
        monkey.take_turn()

print(operator.mul(*heapq.nlargest(2, (monkey.inspection_count for monkey in monkeys))))
