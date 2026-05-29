def find_mirror_planes(g):
    mirror_row = 0
    mirror_column = 0
    midpoint = len(g[0]) // 2
    for c, col in enumerate(g[0]):
        if 0 < c <= midpoint:
            if all(row[:c] == (*reversed(row[c:2*c]),) for row in g):
                mirror_column = c
                break
        if midpoint < c:
            if all(row[c - (len(row) - c):c] == (*reversed(row[c:]),) for row in g):
                mirror_column = len(g[0][:c])
                break
    midpoint = len(g) // 2
    for r, row in enumerate(g):
        if 0 < r <= midpoint:
            if all(tuple(g_row[c] for g_row in g[:r]) == (*reversed(tuple(g_row[c] for g_row in g[r:2*r])),)
                    for c in range(len(g[r]))):
                mirror_row = r
                break
        if midpoint < r:
            if all(tuple(g_row[c] for g_row in g[r - (len(g) - r):r]) == (*reversed(tuple(g_row[c] for g_row in g[r:])),)
                    for c in range(len(g[r]))):
                mirror_row = len(g[:r])
                break
    return (mirror_row, mirror_column)

def find_smudge(g):
    original = find_mirror_planes(g)
    for i, row in enumerate(g):
        mismatches = sum(1 for offset in range(min(i, len(g) - i))
                         for c in range(len(g[0]))
                         if g[i - offset - 1][c] != g[i + offset][c])
        if mismatches == 1:
            return i, 0
    for j in range(len(g[0])):
        mismatches = sum(
            1 for offset in range(min(j, len(g[0]) - j))
            for r in range(len(g))
            if g[r][j - offset - 1] != g[r][j + offset]
        )
        if mismatches == 1:
            return 0, j
    return original

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 13 Advent of Code Input.txt"

with open(file) as f:
    notes = []
    grid = []
    for line in f.readlines():
        if line == '\n':
            notes.append(grid)
            grid = []
        else:
            grid.append((*line.strip(),))
    else:
        notes.append(grid)

summary = sum(find_mirror_planes(tuple(g))[0] * 100 + find_mirror_planes(tuple(g))[1] for g in notes)
c = sum(1 for n in map(find_mirror_planes, notes) if n[0] == 0 or n[1] == 0)
print(f"Part 1: {summary}")

summary = sum(find_smudge(g)[0] * 100 + find_smudge(g)[1] for g in notes)
print(f"Part 2: {summary}")