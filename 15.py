#day 15

import networkx as nx
from copy import copy


def get_input():
    with open('2021/15 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def build_graph(input):
    line = input.pop(0)
    input.insert(0,line)
    row_length = len(line)
    max_num = row_length*row_length

    graph = nx.DiGraph()
    num = 0
    for line in input:
        #print(line)
        for value in line:
            x_pos = num%row_length
            if num-row_length >= 0:
                graph.add_weighted_edges_from([(num-row_length, num, int(value))])
            if x_pos-1 >= 0:
                graph.add_weighted_edges_from([(num-1,  num, int(value))])
            if x_pos < row_length-1:
                graph.add_weighted_edges_from([(num+1,  num, int(value))])
            if num+row_length < max_num-1:
                graph.add_weighted_edges_from([(num+row_length, num, int(value))])
            num += 1

    return graph, num


def extend_cave(input):
    extended_lines = []
    for line in input:
        new_section = ''
        for i in range(1, 5):
            for x in line:
                x = int(x)+i
                if x >= 10:
                    x -= 9
                new_section += str(x)
        extended_lines.append(line + new_section)

    extended_cave = copy(extended_lines)
    for i in range(1, 5):
        for line in extended_lines:
            new_line = ''
            for x in line:
                x = int(x)+i
                if x >= 10:
                    x -= 9
                new_line += str(x)
            extended_cave.append(new_line)

    return extended_cave


#
# part 1
#

graph, number_nodes = build_graph(get_input())
print()

first = 0
last = number_nodes-1

path_length = nx.dijkstra_path_length(graph, first, last)
print("Dijkstra (1): ", path_length)

_pred, dist = nx.dijkstra_predecessor_and_distance(graph, first)
print("Dijkstra (2): ", sorted(dist.items())[-1][1])

path_length = nx.shortest_path_length(graph, source=first, target=last, weight='weight', method='bellman-ford')
print("Bellman-Ford: ", path_length)

_pred, dist = nx.goldberg_radzik(graph, first)
print("Goldberg Radzik: ", sorted(dist.items())[-1][1])

print()


#
# part 2
#

cave = extend_cave(get_input())
graph, number_nodes = build_graph(cave)
print()

first = 0
last = number_nodes-1

path_length = nx.dijkstra_path_length(graph, first, last)
print("Dijkstra (1): ", path_length)

_pred, dist = nx.dijkstra_predecessor_and_distance(graph, first)
print("Dijkstra (2): ", sorted(dist.items())[-1][1])

path_length = nx.shortest_path_length(graph, source=first, target=last, weight='weight', method='bellman-ford')
print("Bellman-Ford: ", path_length)

_pred, dist = nx.goldberg_radzik(graph, first)
print("Goldberg Radzik: ", sorted(dist.items())[-1][1])

print()
