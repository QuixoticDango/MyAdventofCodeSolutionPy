import networkx as nx
from networkx import algorithms

def count_predecessors(node, digraph):
    current_node = node
    s = 0
    if current_node == 'COM':
        return 0
    while current_node != 'COM':
        s += len((list(digraph.predecessors(current_node))))
        current_node = list(digraph.predecessors(current_node))[0]
    return s

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2019 Day 6 Advent of Code Input.txt"

with open(file, "rt") as f:
    orbits = [tuple(line.strip().split(')')) for line in f.readlines()]

graph_of_orbits = nx.DiGraph(orbits)

total_number_of_orbits = 0
for node in graph_of_orbits.nodes:
    total_number_of_orbits += count_predecessors(node, graph_of_orbits)

print(total_number_of_orbits)

graph_of_orbits = graph_of_orbits.to_undirected()

print(len(algorithms.bidirectional_shortest_path(graph_of_orbits, "YOU", "SAN")) - 3)