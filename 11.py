#day 11


import numpy as np

def get_input():
    with open('2021/11 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def build_swarm():
    swarm = []
    for line in get_input():
        swarm.append([int(x) for x in line])
    return swarm


# function 'lent' from Richard
def get_neighbour_locations(x, y):
    return [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]


def flash(swarm, y, x) -> int:
    flashes = 0
    level = swarm[y][x]

    locations = get_neighbour_locations(x, y)

    if level >= 10:
        swarm[y][x] = -999
        flashes += 1

        for _x, _y in locations:
            if _x < 0 or _y < 0 or _x >= len(swarm[0]) or _y >= len(swarm):
                continue

            swarm[_y][_x] += 1
            flashes += flash(swarm, _y, _x)

    return flashes


def print_swarm(swarm):
    for line in swarm:
        print(line)


def solve(steps):
    flashes = 0
    sync_step = -1
    swarm = build_swarm()
    swarm = np.array(swarm)

    for step in range(steps):
        swarm[swarm >= 0] += 1

        for y in range(len(swarm)):
            for x in range(len(swarm[0])):
                flashes += flash(swarm, y, x)

        swarm[swarm <= 0] = 0
        test_synconized = (swarm == 0).all()
        if test_synconized and sync_step == -1:
            sync_step = step+1

    return flashes, sync_step

score, sync = solve(100)
print("Score 1: ", score)

score, sync = solve(240)
print("first sync: ", sync)
