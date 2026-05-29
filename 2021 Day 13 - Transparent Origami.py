def fold(grid:list[list[str]], inst:list[tuple[str, int]]) -> list[list[str]]:
    d, line = inst
    if d == 'x':
        for i, row in enumerate(grid):
            for j, ch in enumerate(row[:line]):
                grid[i][j + 2 * (line - j)] = '#' if grid[i][j] == '#' \
                                                  or grid[i][j + 2 * (line - j)] == '#' else '.'
        return [row[line+1:] for row in grid]
    if d == 'y':
        for i, row in enumerate(grid[line+1:], line+1):
            for j, ch in enumerate(row):
                grid[i + 2 * (line - i)][j] = '#' if grid[i][j] == '#' \
                                                  or grid[i + 2 * (line - i)][j] == '#' else '.'
        return grid[:line]

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 13 Advent of Code Input.txt"

with open(file) as f:
    grid = []
    hash_loc = set()
    instructions = []
    for line in f.readlines():
        if "," in line:
            point = (*map(int, line.strip().split(',')),)
            point = (point[1], point[0])
            hash_loc.add(point)
        if 'f' in line:
            full_line = line.strip().split('=')
            instructions.append((full_line[0][11], int(full_line[1])))
max_row = max(r for r,c in hash_loc)
max_col = max(c for r,c in hash_loc)
# print(max_col)
grid = [['.' for j in range(max_col+1)] for i in range(max_row+1)]
for i, j in hash_loc:
    grid[i][j] = '#'

# print('\n'.join(''.join(ch for ch in row) for row in grid))
# print()
grid = fold(grid, instructions[0])
# print('\n'.join(''.join(ch for ch in row) for row in grid))
# print()
print(f"Part 1: {sum(1 for row in grid for ch in row if ch == '#')}")
for inst in instructions[1:]:
    grid = fold(grid, inst)
# print('\n'.join(''.join(ch for ch in row) for row in grid))
# print()

# print(len(grid[0]))
for i, row in enumerate(grid):
    for j, ch in enumerate(row[:len(row) // 2]):
        # print(f"{j} -> {j + 2 * (len(row) // 2 - j) - 1}")
        grid[i][j], grid[i][j + 2 * (len(row) // 2 - j) - 1] = grid[i][j + 2 * (len(row) // 2 - j) - 1], grid[i][j]
print('\n'.join(''.join(ch for ch in row) for row in grid))
print()
