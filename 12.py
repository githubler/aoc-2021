#day 12



def get_input():
    with open('2021/12 input.txt') as f:
        return [x.strip() for x in f.readlines()]


#
# part 1
#

class Cave():
    visited_twice = False

    def __init__(self, name):
        self.name = name
        self.neighbours = set()
        self.is_visited = False
        if name == name.upper():
            self.is_multiple = True
        else:
            self.is_multiple = False
        if name == 'start':
            self.is_visited = True

    def add_neighbour(self, neighbour):
        self.neighbours.add(neighbour)

    def get_name(self):
        return self.name

    def get_neighbours(self):
        return self.neighbours

    def __str__(self):
        return f'{self.name}'

    def __repr__(self) -> str:
        return str(self)

    def can_visit(self):
        if self.is_visited and not self.is_multiple:
            #if not Cave.visited_twice:
            #    Cave.visited_twice = True
            #    return True
            return False
        else:
            return True

    def visit_neighbours(self):
        num_paths = 0
        if self.name == 'end':
            num_paths = 1
            return num_paths

        self.is_visited = True
        for cave in self.neighbours:
            if cave.can_visit():
                num_paths += cave.visit_neighbours()

        self.is_visited = False
        #Cave.visited_twice = False

        return num_paths



def build_cave_system():
    start = Cave("START")
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




start_cave = build_cave_system()
num_paths = start_cave.visit_neighbours()

print()
print("Submit 1: ", num_paths)

exit(0)






























start-A
start-b
A-c
A-b
b-d
A-end
b-end





dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc





fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW