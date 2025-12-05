from itertools import product

file = "C:\\Users\\DANGO\\Documents\\Coding and Programming Folder\\2025 Day 4 Advent of Code Input.txt"

with open(file, 'rt') as f:
    grid = [row.strip() for row in f.readlines()]

dir = list(product([i for i in range(-1, 2, 1)], repeat=2))
dir = [tup for tup in dir if tup != (0,0)]

accessible_paper_rolls = 0
for i, row in enumerate(grid):
    for j, column in enumerate(row):
        if grid[i][j] != '@':
            continue
        checksum = 0
        for k in range(8):
            try:
                if i + dir[k][0] < 0 or j + dir[k][1] < 0:
                    raise NegativeIndex
                if grid[i + dir[k][0]][j + dir[k][1]] == '@':
                    checksum += 1
            except:
                pass
        if checksum < 4:
            accessible_paper_rolls += 1

print(f"{accessible_paper_rolls=}")
