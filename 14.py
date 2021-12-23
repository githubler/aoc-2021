#day 14

from collections import deque
from collections import Counter
from copy import deepcopy


def get_input():
    with open('2021/14 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def parse_input():
    input = get_input()
    polymer = deque(input.pop(0))
    input.pop(0)

    rules = {}
    for line in input:
        pair, result = line.split(' -> ')
        rules.update({pair: result})

    #print(polymer)
    #print(rules)
    return polymer, rules


def do_part_1():
    polymer, rules = parse_input()
    new_polymer = polymer.copy()
    steps = 10
    for i in range(steps):
        #print("step: ", i)
        polymer = new_polymer.copy()
        for i in range(len(polymer)-1):
            pair = polymer[i]+polymer[i+1]
            if pair in rules:
                result = rules[pair]
                new_polymer.insert((i*2)+1, result)

    counter_polymer = Counter(new_polymer)
    max = counter_polymer.most_common()[0][1]
    min = counter_polymer.most_common()[-1][1]

    return max-min


def do_part_2():
    polymer, rules = parse_input()
    char_counter = Counter(polymer)
    counter = deepcopy(rules)
    for key in counter:
        counter[key] = 0

    for i in range(len(polymer)-1):
        pair = polymer[i]+polymer[i+1]
        if pair in rules:
            counter[pair] += 1

    steps = 40
    for i in range(steps):
        #print("step: ", i)
        new_counter = deepcopy(counter)
        for key, value in counter.items():
            if value:
                new_counter[key[0]+rules[key]] += value
                new_counter[rules[key]+key[1]] += value
                new_counter[key] -= value
                char_counter[rules[key]] += value
        counter = new_counter

    max = char_counter.most_common()[0][1]
    min = char_counter.most_common()[-1][1]

    return max-min

print("Submit 1: ", do_part_1())
print("Submit 2: ", do_part_2())
