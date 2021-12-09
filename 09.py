#day 09

import numpy as np
from skimage.morphology import flood_fill
from bisect import insort


def get_input():
    with open('2021/09 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def build_cave():
    cave = []
    for line in get_input():
        cave.append([int(x) for x in line])
    return cave


#
#part 1
#
def check_min(cave, x, y) -> bool:
    checkpoint = cave[y][x]
    if y == 0:
        up = 10
    else:
        up = cave[y-1][x]

    if y < len(cave) - 1:
        down = cave[y+1][x]
    else:
        down = 10

    if x == 0:
        left = 10
    else:
        left = cave[y][x-1]

    if x < len(cave[0]) -1 :
        right = cave[y][x+1]
    else:
        right = 10

    if checkpoint < min(up, down, left, right):
        return True

    return False


def solve_part1() -> int:
    sum = 0
    cave = build_cave()

    for y in range(len(cave)):
        for x in range(len(cave[0])):
            if check_min(cave, x, y):
                risk_level = cave[y][x] + 1
                sum += risk_level

    return sum


#
# part 2
#
def solve_part2() -> int:
    cave = build_cave()
    cave = np.array(cave)
    cave[cave < 9] = 0

    sums = []
    num_basin = 0

    for y in range(len(cave)):
        for x in range(len(cave[0])):
            if cave[y][x] == 0:
                num_basin -= 1
                # fill with negative numbers (num_basin)
                cave = flood_fill(cave, (y, x), num_basin, connectivity=1)
                sum_basin = cave[cave == num_basin].sum() / num_basin
                insort(sums, sum_basin)

    return sums



submit = solve_part1()
print("Submit part1: ", submit)

basins = solve_part2()
submit = basins[-1] * basins[-2] * basins[-3]
print("Submit part1: ", submit)
