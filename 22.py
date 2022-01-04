#day 22


import re
import numpy as np


def get_input():
    with open('2021/22 input.txt') as f:
        return [x.strip() for x in f.readlines()]

def do_part_1():
    regex = re.compile('(on|off) x=(-?[0-9]+)\.\.(-?[0-9]+),y=(-?[0-9]+)\.\.(-?[0-9]+),z=(-?[0-9]+)\.\.(-?[0-9]+)')
    cube = np.zeros((101, 101, 101))

    for line in get_input():
        on_off, x_min, x_max, y_min, y_max, z_min, z_max = re.match(regex, line).groups()

        x_min = int(x_min)
        x_max = int(x_max)
        y_min = int(y_min)
        y_max = int(y_max)
        z_min = int(z_min)
        z_max = int(z_max)

        if x_min < -50 or y_min < -50 or z_min < -50 or x_max > 50 or y_max > 50 or z_max > 50:
            continue

        x_min +=50
        x_max +=50
        y_min +=50
        y_max +=50
        z_min +=50
        z_max +=50

        if on_off == 'on':
            for z in range(z_min, z_max+1):
                for y in range(y_min, y_max+1):
                    for x in range(x_min, x_max+1):
                        cube[z, y, x] = 1.
        else:
            for z in range(z_min, z_max+1):
                for y in range(y_min, y_max+1):
                    for x in range(x_min, x_max+1):
                        cube[z, y, x] = 0.

    return cube.sum()

#
# part 2
#
def create_cuboids():
    regex = re.compile('(on|off) x=(-?[0-9]+)\.\.(-?[0-9]+),y=(-?[0-9]+)\.\.(-?[0-9]+),z=(-?[0-9]+)\.\.(-?[0-9]+)')
    parsed_data = [re.match(regex, line).groups() for line in get_input()]

    cuboids = []
    for data in parsed_data:
        cuboid = []
        for i in range(7):
            if i==0:
                if data[0] == 'on':
                    cuboid.append(1)
                else:
                    cuboid.append(-1)
            else:
                cuboid.append(int(data[i]))
        cuboids.append(cuboid)
    return cuboids

def intersection(cuboid_1, cuboid_2):
    new_cuboid = []
    new_cuboid.append(cuboid_2[0]*-1)
    new_cuboid.append(max(cuboid_1[1], cuboid_2[1]))
    new_cuboid.append(min(cuboid_1[2], cuboid_2[2]))
    new_cuboid.append(max(cuboid_1[3], cuboid_2[3]))
    new_cuboid.append(min(cuboid_1[4], cuboid_2[4]))
    new_cuboid.append(max(cuboid_1[5], cuboid_2[5]))
    new_cuboid.append(min(cuboid_1[6], cuboid_2[6]))
    return None if new_cuboid[1] > new_cuboid[2] or new_cuboid[3] > new_cuboid[4] or new_cuboid[5] > new_cuboid[6] else new_cuboid

def do_part_2():
    cuboids = create_cuboids()

    # |(AvB)vC| = (|A|+|B|-|A^B|) + |C| - |A^C| - |A^B| + |A^B^C|
    initialization_steps = []
    for cuboid in cuboids:
        new_steps_to_add = []
        if cuboid[0] == 1:
            new_steps_to_add += [cuboid]

        for step in initialization_steps:
            new_step = intersection(cuboid, step)
            if new_step:
                new_steps_to_add += [new_step]
        initialization_steps += new_steps_to_add

    # count 'ON' cubes
    counter = 0
    for step in initialization_steps:
        # volume of cuboid(=step)
        count = (step[2]-step[1]+1) * (step[4]-step[3]+1) * (step[6]-step[5]+1)
        # cuboid 'ON' or 'OFF'
        counter += (step[0]*count)

    return counter


sum = do_part_1()
print("Submit part1: ", sum)

sum = do_part_2()
print("Submit part2: ", sum)
