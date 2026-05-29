from collections import deque
import sys

def bfs(h: list[str], root: tuple[int, int], q: deque = None, visited: set = None) -> list:
    if q is None:
        q = deque()
    if visited is None:
        visited = set()

    q.append(root)
    visited.add(root)
    steps: int = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if (i, j) == e_loc:
                return steps
            for di, dj in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(h) and 0 <= nj < len(h[0]):
                    if ord(h[ni][nj]) - ord(h[i][j]) <= 1 \
                        and (ni, nj) not in visited:
                        q.append((ni, nj))
                        visited.add((ni, nj))
        steps += 1
    return -1

file: str = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 12 Advent of Code Input.txt"

with open(file) as f:
    hill: list[str] = f.read().splitlines()

s_loc = next((i,j) for i, row in enumerate(hill) for j, ch in enumerate(row) if ch =='S')
e_loc = next((i,j) for i, row in enumerate(hill) for j, ch in enumerate(row) if ch =='E')
hill[s_loc[0]] = hill[s_loc[0]].replace('S', 'a')
hill[e_loc[0]] = hill[e_loc[0]].replace('E', 'z')

d = [(-1,0),(1,0),(0,-1),(0,1)]
# print(f"Part 1: {bfs(hill, s_loc)}")

# The following also works using networkx
import networkx as nx

edges: list[tuple[tuple[int, int]]] = []
for i, row in enumerate(hill):
    for j, ch in enumerate(row):
        for di, dj in d:
            if 0 <= i + di < len(hill) and 0 <= j + dj < len(row):
                if ord(hill[i+di][j+dj]) - ord(ch) <= 1:
                    edges.append(((i,j),(i+di, j+dj)))

graph = nx.DiGraph()
graph.add_edges_from(edges)

all_as = [(i,j) for i, row in enumerate(hill) for j, ch in enumerate(row) if ch == 'a']
print(f"Part 1: {nx.shortest_path_length(graph, source=s_loc, target=e_loc)}")
min_path = sys.maxsize
for loc in all_as:
    try:
        path = nx.shortest_path_length(graph, source=loc, target=e_loc)
        if path < min_path:
            min_path = path
    except nx.NetworkXNoPath as e:
        pass
print(f"Part 2: {min_path}")

print(f"Part BFS: {min(bfs(hill, loc) for loc in all_as if bfs(hill, loc) != -1)}")