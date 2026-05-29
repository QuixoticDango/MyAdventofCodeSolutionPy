import networkx as nx
import re
from collections import defaultdict
from copy import deepcopy

file: str = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 7 Advent of Code Input.txt"

with open(file) as f:
    edges: list = []
    curr_path: list = ['/']
    curr_dir: str = None
    prev_dir: str = None
    listing_contents: bool = False
    paths: defaultdict[int] = defaultdict(int)

    for i, line in enumerate(f.read().splitlines()):
        if "$ cd" in line:
            listing_contents = False
            direction = line[5:]
            if direction == '/':
                curr_path = ['/']
            elif direction == '..':
                curr_path.pop()
                    # break
            else:
                curr_path.append(direction)
        if "$ ls" in line:
            listing_contents = True
            continue
        if listing_contents:
            size, name = line.split()
            if size.isnumeric():
                size = int(size)
            else: 
                continue
            temp_path = deepcopy(curr_path)
            while temp_path:
                paths['/'.join(temp_path)] += size
                temp_path.pop()

score = sum(size for path, size in paths.items() if size <= 100000)
print(f"Part 1: {score}")

d_lst = [(k,v) for k,v in paths.items()]
d_lst.sort(key=lambda s: s[1])
unused_space = 70000000 - d_lst[-1][1]
s = 0
for path, size in d_lst:
    if size + unused_space >= 30000000:
        s = size
        break
print(f"Part 2: {s}")