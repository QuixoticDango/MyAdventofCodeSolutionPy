# import re

# def shortestPath(l, d):
#     minDist = 0
#     visited = set()
#     i = 0
#     while len(visited) != len(l):
#         for key in d.keys():
#             for loc in l:
#             minDist += min(d[(l1,l2)] for l1,l2 in d.keys() for loc in l if loc == l1 or loc == l2 and loc not in visited)
#             visited.add(l1)
#             visited.add(l2)
#     return minDist



# filePath ="C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 9 Advent of Code Input.txt"
# with open(filePath, 'r') as f:
#     distances = {tuple(line[:re.search(' =', line).start()].split(' to ')):
#                  int(line[re.search(r"\d+", line).start():re.search(r"\d+", line).end()])
#                  for line in f.readlines()}

# locations = []
# for l1, l2 in distances.keys():
#     if l1 not in locations:
#         locations.append(l1)
#     if l2 not in locations:
#         locations.append(l2)
# print(shortestPath(locations, distances))

import sys
from itertools import permutations

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 9 Advent of Code Input.txt"
places = set()
distances = dict()
for line in open(filePath):
    (source, _, dest, _, distance) = line.split()
    places.add(source)
    places.add(dest)
    distances.setdefault(source, dict())[dest] = int(distance)
    distances.setdefault(dest, dict())[source] = int(distance)

shortest = sys.maxsize
longest = 0
for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print("shortest: %d" % (shortest))
print("longest: %d" % (longest))