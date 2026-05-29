def find_out(d, paths=0, key='you'):
    if key == 'out':
        paths += 1
        return paths

    for k in d[key]:
        if key == 'out':
            continue
        key = k
        return find_out(d, paths, key)

file = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2025 Day 11 Advent of Code Input.txt"

with open(file, 'rt') as f:
    devices = {line.strip().split()[0][:-1]:line.strip().split()[1:] for line in f.readlines()}

# print(find_out(devices))

from functools import cache

def part1(puzzle_input):
    connections = puzzle_input
    
    @cache
    def dfs(device):
        if device == "out":
            return 1
        if (outputs := connections.get(device)) is None:
            return 0
        return sum(dfs(out) for out in outputs)

    return dfs('you')
print(part1(devices))