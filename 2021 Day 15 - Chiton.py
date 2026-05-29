# import heapq as hq
# from numpy import inf
# import networkx as nx
# from itertools import combinations

# def in_bounds(p: tuple[int, int]) -> bool:
#     if 0 <= p[0] < max(i for i,j in nodes) and 0 <= p[1] < max(j for i,j in nodes):
#         return True
#     return False

# # def traverse_grid(g: tuple[tuple[int]], curr_pos: tuple[int, int] = (0,0),
# #                   curr_dir: tuple[int, int] = (1, 0), visited: set = None, risk: int = 0,
# #                   rounds:int = 0) -> int:
    
# #     if visited is None:
# #         visited = set()
    
# #     visited.add(curr_pos)

# #     i, j = curr_pos
# #     di, dj = curr_dir
# #     new_pos = (i + di, j + dj)

# #     if not in_bounds(new_pos, g) or new_pos in visited:
# #         new_dir = d[(d.index(curr_dir) + 1) % 4]
# #         return traverse_grid(g, curr_pos, new_dir, visited, risk, rounds)

# #     if rounds > 0:
# #         risk += grid[i][j]

# #     if curr_pos == (len(grid) - 1, len(grid[0]) - 1):
# #         return risk
# #     return traverse_grid(g, new_pos, curr_dir, visited, risk, rounds)
    
# # def traverse_grid(node: tuple[int, int] = (0, 0), visited: set = None, check:int = 0)-> int:
# #     if visited is None:
# #         visited = list()
# #     visited.append(node)
# #     if node == (max(i for i,j in nodes) - 1, max(j for i, j in nodes) - 1):
# #         return visited
# #     check_nodes = []
# #     for di, dj in directions:
# #         new_node = (node[0] + di, node[1] + dj)
# #         if in_bounds(new_node) and new_node not in visited:
# #             cumulative_risk = nodes[node] + nodes[new_node]
# #             nodes[new_node] = cumulative_risk
# #             check_nodes.append((new_node[0], new_node[1], nodes[new_node]))
# #     if 4 < check < 7:
# #         print(f"{check = } | {check_nodes = }")
# #     min_node = next(n for n in check_nodes if n[2] == min(r for i, j, r in check_nodes))
# #     return traverse_grid((min_node[0], min_node[1]), visited, check=check + 1)

# def Dijkstra(G:nx.Graph, start_node: tuple[int, int, int] = (0, 0, 0)):
#     for node in G:

# file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 15 Advent of Code Input.txt"

# with open(file) as f:
#     nodes = [
#         [0, i, j] if i == 0 and j == 0 else [int(ch), i, j]
#         for i, row in enumerate(f.readlines()) 
#         for j, ch in enumerate(row.strip())
#         ]

# heap = [(i, j) for r, i, j in nodes]
# hq.heapify(hea

# unvisited = {(i, j) for r, i, j in nodes if i > 0 or j > 0}
# edges_with_risk = [
#     (tuple(lst1), tuple(lst2)) for lst1, lst2 in combinations(nodes, 2)
#     if lst1[1] == lst2[1] and abs(lst1[2] - lst2[2]) == 1 or
#     lst1[2] == lst2[2] and abs(lst1[1] - lst2[1]) == 1
#     ]
# graph = nx.Graph()
# graph.add_edges_from(edges_with_risk)
# # for edge in graph.edges:
# #     print(edge)
# # point_edges
# print(len(unvisited))
# unaltered_nodes = [entry[:] for entry in nodes]
# # hq.heapify(nodes)
# # print(nodes)
# # unvidsited = {node for row in nodes for node in row}
# directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# # path = traverse_grid()
# # print(path)
# # total_risk = sum(nodes[key] for key in path)
# # print(f"Part 1: {total_risk}")

# From AI

from heapq import heappop, heappush

def traverse_grid(g:list[list[int]], h:list[tuple[int,int,int]], di:list[list[int | float]]):
    while h:
        # print(f"Round {rounds}: {h}")
        risk, r, c = heappop(h)

        # If we reached the end, we're done
        if r == rows - 1 and c == cols - 1:
            # print("Part 1:", risk)
            # break
            return risk
        # Skip if we've already found a better path to (r, c)
        if risk > di[r][c]:
            continue

        # Explore neighbors
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:  # In bounds
                new_risk = risk + g[nr][nc]
                if new_risk < di[nr][nc]:  # Found a better path
                    di[nr][nc] = new_risk
                    heappush(h, (new_risk, nr, nc))

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 15 Advent of Code Input.txt"

with open(file) as f:
    grid = [[int(ch) for ch in line.strip()] for line in f.readlines()]

original = [row[:] for row in grid]
# Grid dimensions
rows, cols = len(grid), len(grid[0])

dirs = [(-1,0),(1,0),(0,-1),(0,1)]

# Priority queue: (total_risk, row, col)
heap = [(0,0,0)] # Start at (0,0) with 0 risk so far

# Distance matrix: short risk to reach each cell
dist = [[float('inf')] * cols for _ in range(rows)]
dist[0][0] = 0

print(f"Part 1: {traverse_grid(grid, heap, dist)}")
R, C = len(original), len(original[0])
new_grid = [[(original[i % R][j % C] + i // R + j // C - 1) % 9 + 1 for j in range(C * 5)]
            for i in range(R * 5)]

rows, cols = len(new_grid), len(new_grid[0])
dist = [[float('inf')] * cols for _ in range(rows)]
dist[0][0] = 0
heap = [(0,0,0)]
print('\n'.join(''.join(str(n) for n in row) for row in new_grid))
print(f"Part 2: {traverse_grid(new_grid, heap, dist)}")