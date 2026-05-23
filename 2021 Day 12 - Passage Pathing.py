import networkx as nx
from collections import defaultdict
from sys import maxsize

def modified_dfs(G:nx.Graph, start_node:str = "start", end_node:str = "end",
                 path:list = None, max_depth:int = 100):
    if path is None:
        path = []
    path = path + [start_node]

    if start_node == end_node:
        return [path]
    if len(path) > max_depth:
        return []
    
    paths = []
    for neighbor in G.neighbors(start_node):
        if neighbor == "start":
            continue
        if all(ch.islower() for ch in neighbor) and neighbor in path:
            continue
        new_paths = modified_dfs(G, neighbor, end_node, path, max_depth)
        paths.extend(new_paths)
    return paths


# Failed part 2. Try to better understand recursion here.
def modified_dfs_2(G, start_node="start", end_node="end", path=None, visit_count=None):
    if visit_count is None:
        visit_count = defaultdict(int)
    else:
        visit_count = visit_count.copy()

    if path is None:
        path = []

    # Check termination conditions first
    if start_node == "end":
        return [path + ["end"]]
    if start_node == "start" and path:
        return []  # Can't revisit start

    # Check if this would violate visit rules
    if start_node.islower():
        if visit_count[start_node] >= 1:
            # Already visited once; second visit only allowed if no other cave has been doubled
            if any(v >= 2 for v in visit_count.values()):
                return []  # Another cave already visited twice
        # Allow second visit to this small cave

    # Now update state
    new_path = path + [start_node]
    new_visit_count = visit_count.copy()
    if start_node.islower():
        new_visit_count[start_node] += 1

    paths = []
    for neighbor in G.neighbors(start_node):
        new_paths = modified_dfs_2(G, neighbor, end_node, new_path, new_visit_count)
        paths.extend(new_paths)

    return paths   

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 12 Advent of Code Input.txt"

with open(file) as f:
    edges = [tuple(line.strip().split('-')) for line in f.readlines()]
caves = nx.Graph()
caves.add_edges_from(edges)

p = modified_dfs(caves)

print(f"Part 1: {len(modified_dfs(caves))}")
print(f"Part 2: {len(modified_dfs_2(caves))}")