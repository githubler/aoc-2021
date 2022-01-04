#day 22


from os import X_OK
import re
import numpy as np


def get_input():
    with open('22 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def do_part_1():
    regex = re.compile('(on|off) x=(-?[0-9]+)\.\.(-?[0-9]+),y=(-?[0-9]+)\.\.(-?[0-9]+),z=(-?[0-9]+)\.\.(-?[0-9]+)')

    cube = np.zeros((100, 100, 100))

    for line in get_input():
        #match = re.match(regex_on_off_x, line).groups()
        #print(match[0])
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


sum = do_part_1()
print("Submit: ", sum)

