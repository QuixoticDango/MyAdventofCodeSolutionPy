file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2020 Day 3 Advent of Code Input.txt"

def trace_path(g, step=(1,3)):
    length = len(g)
    width = len(g[0])
    curr_pos = (0,0)
    trees = 0
    while curr_pos[0] < len(g)-1:
        curr_pos = ((curr_pos[0] + step[0]) % length, (curr_pos[1] + step[1]) % width)
        try:
            if g[curr_pos[0]][curr_pos[1]] == "#":
                trees += 1
        except IndexError:
            print(f"{curr_pos}")
    return trees

def product(lst):
    p = 1
    for n in lst:
        p *= n
    return p

with open(file) as f:
    grid = [[ch for ch in line.strip()] for line in f.readlines()]

steps = [(1, i) for i in range(8) if i % 2 == 1] + [(2, 1)]
print(f"Part 1: {trace_path(grid)}")
print(f"Part 2: {product([trace_path(grid, step) for step in steps])}")