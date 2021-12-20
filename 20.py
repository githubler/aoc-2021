#day 20

from copy import deepcopy


def get_input():
    with open('2021/20 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def parse_input():
    input = get_input()
    iea = input.pop(0)
    input.pop(0)
    line = input.pop(0)
    input.insert(0,line)

    image = []
    for line in input:
        row = []
        for i in line:
            if i == '#':
                row += '1'
            else:
                row += '0'
        image.append(row)

    return iea, image


def extend_image(image, iea, odd_times):
    extended_image = []
    size = len(image)
    if not odd_times and iea[0] == '#':
        zero_line = ['1' for i in range(size+4)]
    else:
        zero_line = ['0' for i in range(size+4)]
    extended_image.append(zero_line)
    extended_image.append(deepcopy(zero_line))
    for line in image:
        if not odd_times and iea[0] == '#':
            row = ['1', '1']
        else:
            row = ['0', '0']
        for i in line:
            row += i
        if not odd_times and iea[0] == '#':
            row += ['1', '1']
        else:
            row += ['0', '0']
        extended_image.append(row)
    extended_image.append(deepcopy(zero_line))
    extended_image.append(deepcopy(zero_line))

    return extended_image


def do_iea(x, y, iea, image):
    binary_str = ''
    binary_str += image[y-1][x-1]
    binary_str += image[y-1][x]
    binary_str += image[y-1][x+1]
    binary_str += image[y][x-1]
    binary_str += image[y][x]
    binary_str += image[y][x+1]
    binary_str += image[y+1][x-1]
    binary_str += image[y+1][x]
    binary_str += image[y+1][x+1]

    num = int(binary_str, 2)
    if iea[num] == '#':
        return '1'
    else:
        return '0'


def enhance_image(image):
    size = len(image)
    enhanced_image = deepcopy(image)

    for y in range(size):
        for x in range(size):
            if x == 0 or y == 0 or x == size-1 or y == size-1:
                if image[0][0] == '0':
                    if iea[0] == '#':
                        enhanced_image[y][x] = '1'
                    else:
                        enhanced_image[y][x] = '0'
                else:
                    if iea[511] == '#':
                        enhanced_image[y][x] = '1'
                    else:
                        enhanced_image[y][x] = '0'
            else:
                result = do_iea(x, y, iea, image)
                enhanced_image[y][x] = result

    return enhanced_image


def count_lit_pixels(image):
    count = 0
    for i in image:
        count += i.count('1')

    return count


#
# part 1 & 2
#

iea, enhanced_image = parse_input()
odd_times = True
for i in range(50):
    image = extend_image(enhanced_image, iea, odd_times)
    enhanced_image = enhance_image(image)
    if odd_times:
        odd_times = False
    else:
        odd_times = True

lit_pixels = count_lit_pixels(enhanced_image)
print("Submit: ", lit_pixels)