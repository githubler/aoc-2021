# day 06

from collections import deque

def get_input():
    with open('2021/06 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def solve(days):
    fishes = [int(x) for x in get_input()[0].split(',')]
    ages = deque([0,0,0,0,0,0,0,0,0])
    for x in range(len(fishes)):
        ages[fishes[x]] += 1

    for day in range(0, days):
        ages.rotate(-1)
        ages[6] += ages[8]

    return sum(ages)


# part 1
days = 80
submit = solve(days)
print("Submit - part 1: ", submit)

# part 2
days = 256
submit = solve(days)
print("Submit - part 2: ", submit)
