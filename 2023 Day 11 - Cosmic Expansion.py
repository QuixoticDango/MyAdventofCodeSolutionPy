from itertools import combinations

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 11 Advent of Code Input.txt"

def manhattan_distance(p1, p2):
    r_dist = abs(p2[0] - p1[0])
    c_dist = abs(p2[1] - p1[1])
    return r_dist + c_dist

def map_location(loc, expansion_coefficient):
    empty_cols_preceding_loc = sum(1 for col in range(loc[1])
                                   if all(unexpanded_universe[row][col] == '.'
                                          for row in range(len(unexpanded_universe))))
    empty_rows_preceding_loc = sum(1 for row in range(loc[0])
                                   if all(unexpanded_universe[row][col] == '.'
                                          for col in range(len(unexpanded_universe[0]))))
    new_row = loc[0] + empty_rows_preceding_loc * (expansion_coefficient - 1)
    new_col = loc[1] + empty_cols_preceding_loc * (expansion_coefficient - 1)
    return (new_row, new_col)

with open(file) as f:
    universe = [[ch for ch in line.strip()] for line in f.readlines()]
# print(universe)
unexpanded_universe = [row[:] for row in universe]
# Expand empty columns
col = 0
while col < len(universe[0]):
    if all(row[col] == '.' for row in universe):
        print("FOUND COLUMN")
        for r, row in enumerate(universe):
            universe[r].insert(col, '.')
        col += 2
    else:
        col += 1

row = 0
while row < len(universe):
    if all(ch == '.' for ch in universe[row]):
        print("FOUND ROW")
        universe.insert(row, ['.',] * len(universe[0]))
        row += 2
    else:
        row += 1

galaxy_locations = [(r, c) for r, row in enumerate(universe) for c, col in enumerate(row) if universe[r][c] == '#']
pair_dist_sum = sum(manhattan_distance(p1, p2) for p1, p2 in combinations(galaxy_locations, 2))
print('\n'.join(''.join(ch for ch in row) for row in universe))
print()
print('\n'.join(''.join(ch for ch in row) for row in unexpanded_universe))
print(f"Part 1: {pair_dist_sum}")

# Part 2
pair_dist_sum = 0
galaxy_locations = [(r, c) for r, row in enumerate(unexpanded_universe) for c, col in enumerate(row) if unexpanded_universe[r][c] == '#']
for a, b in combinations(galaxy_locations, 2):
    p1 = map_location(a, 1000000)
    p2 = map_location(b, 1000000)
    pair_dist_sum += manhattan_distance(p1, p2)
print(f"Part 2: {pair_dist_sum}")
# 1315421415046 is too high