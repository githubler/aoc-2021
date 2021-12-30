#day 17


# Test
# target area: x=20..30, y=-10..-5
x_min = 20
x_max = 30
y_min = -10
y_max = -5

# Task
#target area: x=192..251, y=-89..-59
x_min = 192
x_max = 251
y_min = -89
y_max = -59


#
# part 1 & 2
#
def check(x,y):
    if x<=x_max and x>=x_min and y<=y_max and y>=y_min:
        return True
    return False


max_height_game = 0
counter = 0
for x_start in range(0, x_max+1):
    for y_start in range(y_min, 300):
        x_vel = x_start
        y_vel = y_start
        x = 0
        y = 0
        max_height = 0
        while x<=x_max and y>=y_min:
            x += x_vel
            y += y_vel
            max_height = max(y, max_height)
            if x_vel != 0:
                x_vel -= 1
            y_vel -= 1

            if check(x, y):
                max_height_game = max(max_height_game, max_height)
                counter += 1
                print(x_start, y_start, max_height_game, counter)
                print("Submit: ", max_height_game, counter)
                break

print()
print("END")