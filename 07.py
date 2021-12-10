#day 07


def get_input():
    with open('2021/07 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def calc_fuel_part1():
    positions = [int(x) for x in get_input()[0].split(',')]
    #print((positions))
    fuel_used = []
    for pos in range(len(positions)):
        sum = 0
        for x in range(len(positions)):
            sum = sum + abs(positions[x] - (pos+1))
        fuel_used.append(sum)
        #print(fuel_used)

    return fuel_used


def calc_fuel_part2():
    positions = [int(x) for x in get_input()[0].split(',')]
    #print((positions))
    fuel_used = []
    for pos in range(len(positions)):
        sum = 0
        for x in range(len(positions)):
            n = abs(positions[x] - (pos+1)) + 1
            sum = sum + (n*(n-1)/2)
        fuel_used.append(sum)
        #print(fuel_used)

    return fuel_used

consumption = calc_fuel_part1()
minimum = min(consumption)
print("Submit part1: ", minimum)

consumption = calc_fuel_part2()
minimum = min(consumption)
print("Submit part2: ", minimum)
