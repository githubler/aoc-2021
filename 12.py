#day 12


def get_input():
    with open('12 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def build_cave_system():
    caves = {}

    for line in get_input():
        name_1, name_2 = line.strip().split("-")
        if name_1 in caves and name_2 in caves:
            caves[name_1].add_neighbour(caves[name_2])
            caves[name_2].add_neighbour(caves[name_1])
        elif name_1 in caves and name_2 not in caves:
            new_cave = Cave(name_2)
            caves[name_2] = new_cave
            caves[name_1].add_neighbour(new_cave)
            new_cave.add_neighbour(caves[name_1])
        elif name_1 not in caves and name_2 in caves:
            new_cave = Cave(name_1)
            caves[name_1] = new_cave
            caves[name_2].add_neighbour(new_cave)
            new_cave.add_neighbour(caves[name_2])
        else:
            new_cave_1 = Cave(name_1)
            new_cave_2 = Cave(name_2)
            caves[name_1] = new_cave_1
            caves[name_2] = new_cave_2
            new_cave_1.add_neighbour(new_cave_2)
            new_cave_2.add_neighbour(new_cave_1)

    return caves['start']


class Cave():
    def __init__(self, name):
        self.name = name
        self.neighbours = set()
        if name == name.upper():
            self.multiple = True
        else:
            self.multiple = False

    def add_neighbour(self, neighbour):
        self.neighbours.add(neighbour)

    def is_start(self):
        return 'start' == self.name

    def is_small_cave(self):
        return self.name[0].islower()

    def get_name(self):
        return self.name

    def is_multiple(self):
        return self.multiple

    def __str__(self):
        return f'{self.name}'

    def __repr__(self) -> str:
        return str(self)

    def visit_neighbours(self, visited, vis_twice=False):
        num_paths = 0
        if self.name == 'end':
            num_paths = 1
            return num_paths

        visited += [self.name]
        for cave in self.neighbours:
            if cave.is_start():
                continue

            if not (cave.get_name() in visited and not cave.is_multiple()):
                num_paths += cave.visit_neighbours(visited, vis_twice)
            elif cave.is_small_cave() and vis_twice==True and not cave.is_start():
                num_paths += cave.visit_neighbours(visited, False)

        visited.pop()
        return num_paths


# build cave system for part 1&2
start_cave = build_cave_system()

#
# part 1
#
num_paths = start_cave.visit_neighbours([])

print()
print("Submit 1: ", num_paths)

#
# part 2
#
num_paths = start_cave.visit_neighbours([], True)

print()
print("Submit 2: ", num_paths)
