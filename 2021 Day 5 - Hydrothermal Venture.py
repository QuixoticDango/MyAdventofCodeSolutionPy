from collections import defaultdict, Counter
from time import time
from fractions import Fraction
s = time()

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 5 Advent of Code Input.txt"

with open(file) as f:
    lines = list(tuple(map(eval, line.strip().split(' -> '))) for line in f.readlines())

crossed = []
points = {'hrz':defaultdict(list), 'vrt':defaultdict(list)}
HV_lines = set(filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], lines))
for p1, p2 in filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], lines):
    if p1[0] == p2[0]:
        for j in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
            crossed.append((p1[0], j))
    if p1[1] == p2[1]:
        for i in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
            crossed.append((i, p1[1]))
counts = Counter(crossed)
result = sum(1 for key, val in counts.items() if val > 1)
print(f"Part 1: {result}")

counts = None
result = 0
crossed = []
for p1, p2 in lines:
    x1, y1 = p1
    x2, y2 = p2
    dx = 0 if x1 == x2 else (1 if x2 > x1 else -1)
    dy = 0 if y1 == y2 else (1 if y2 > y1 else -1)
    
    # Only process if horizontal, vertical, or 45-degree diagonal
    if dx == 0 or dy == 0 or abs(x1 - x2) == abs(y1 - y2):
        x, y = x1, y1
        while True:
            crossed.append((x, y))
            if x == x2 and y == y2:
                break
            x += dx
            y += dy

counts = Counter(crossed)
result = sum(1 for key, val in counts.items() if val > 1)
print(f"Part 2: {result}")

print(f"{(time() - s) * 1000} ms")