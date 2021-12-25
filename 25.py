#day 25



def get_input():
    with open('2021/25 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def build_seafloor():
    floor = []
    for line in get_input():
        floor.append(line)

    return floor


def make_new_row(floor):
    new_row = []
    for i in range(len(floor[0])):
        new_row += '.'
    return new_row


def move_east(floor):
    moving = False
    new_floor = []
    for row in floor:
        new_row = make_new_row(floor)
        #print(row)
        for pos in reversed(range(len(row))):
            next_pos = (pos+1) % (len(row))
            if row[pos] == '>' and row[next_pos] == '.':
                new_row[next_pos] = '>'
                moving = True
            elif row[pos] != '.':
                new_row[pos] = row[pos]
        #print(new_row)
        new_floor.append(new_row)
    #print(new_floor)
    return new_floor, moving


def move_south(floor):
    moving = False
    new_floor = []
    for _ in range(len(floor)):
        new_floor.append(make_new_row(floor))
    #print(new_floor)

    for x in range(len(floor[0])):
        #new_row = make_new_row(floor)
        #print(row)
        for pos in reversed(range(len(floor))):
            next_pos = (pos+1) % (len(floor))
            if floor[pos][x] == 'v' and floor[next_pos][x] == '.':
                new_floor[next_pos][x] = 'v'
                moving = True
            elif floor[pos][x] != '.':
                new_floor[pos][x] = floor[pos][x]
        #print(new_row)
    return new_floor, moving


#
# part 1
#
floor = build_seafloor()

is_moving = True
step = 0
while is_moving:
    floor, moving = move_east(floor)
    is_moving &= moving
    floor, moving = move_south(floor)
    is_moving |= moving
    step += 1
    print("Step: ", step)
    for line in floor:
        out = ''
        for c in line:
            out += c
        print(out)
    print()

print("Step: ", step)