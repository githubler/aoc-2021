#day 13

import numpy as np

def get_input():
    with open('2021/13 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def build_matrix_recipes():
    coordinates = []
    recipes = []
    max_x = max_y = 0
    for line in get_input():
        if line:
            if line.startswith('fold'):
                fold, along, axis_value = line.split()
                axis, value = axis_value.split('=')
                recipes.append([axis, int(value)])
            else:
                x, y = line.split(',')
                if int(x) > max_x: max_x = int(x)
                if int(y) > max_y: max_y = int(y)
                coordinates.append([int(x), int(y)])

    matrix = np.zeros((max_y+1, max_x+1))
    for coord in coordinates:
        matrix[coord[1], coord[0]] = 1

    return matrix, recipes


def fold(matrix, recipes):
    y_max = len(matrix)
    x_max = len(matrix[0])
    for recipe in recipes:
        if recipe[0] == 'x':
            for y in range(0, y_max):
                for x in range(recipe[1]):
                    _x = x_max-1-x
                    if matrix[y, _x] == 1:
                        matrix[y, _x] = 0
                        matrix[y, x] = 1
            x_max = x+1
        else:
            for y in range(0, recipe[1]):
                _y = y_max-1-y
                for x in range(x_max):
                    if matrix[_y, x] == 1:
                        matrix[_y, x] = 0
                        matrix[y, x] = 1
            y_max = y+1

    return matrix, x_max, y_max


#
# part 1
#
matrix, recipes = build_matrix_recipes()
matrix = fold(matrix, [recipes[0]])
sum = matrix[matrix == 1].sum()

print("Submit 1: ", sum)
print()


#
# part 2
#
matrix, recipes = build_matrix_recipes()
matrix, x_max, y_max = fold(matrix, recipes)

for y in range(0, y_max+1):
    line = ''
    for x in range(0, x_max+1):
        if matrix[y, x] == 0:
            line += '.'
        else:
            line += '#'
    print(line)
