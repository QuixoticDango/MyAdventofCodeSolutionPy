def size_basin(basin: list[tuple[int, int]] = [], count: int = 1) -> int:
    points_added = False
    for point in basin:
        i, j = point
        for k, d in enumerate(directions):
            if i+d[0] < 0 or j+d[1] < 0:
                continue
            if i+d[0] >= len(grid) or j+d[1] >= len(row):
                continue
            if grid[i+d[0]][j+d[1]] == 9:
                continue
            if grid[i+d[0]][j+d[1]] - grid[i][j] == 1 and (i+d[0],j+d[1]) not in basin:
                basin.append((i+d[0], j+d[1]))
                points_added = True
            if grid[i+d[0]][j+d[1]] - grid[i][j] > 1 and (i+d[0],j+d[1]) not in basin:
                basin.append((i+d[0], j+d[1]))
                points_added = True
    if not points_added:
        return len(basin)
    else:
        return size_basin(basin, count = count + 1)

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 9 Advent of Code Input.txt"

with open(file) as f:
    grid = [[int(ch) for ch in line.strip()] for line in f.readlines()]
s = 0

directions = [(-1,0), (1,0), (0,-1), (0,1)]
low_points = set()
for i, row in enumerate(grid):
    for j, ch in enumerate(row):
        for k, d in enumerate(directions):
            if i+d[0] < 0 or j+d[1] < 0:
                continue
            if i+d[0] >= len(grid) or j+d[1] >= len(row):
                continue
            if ch >= grid[i+d[0]][j+d[1]]:
                break
        else:
            low_points.add((i,j))
            s += 1 + int(ch)
print(f"Part 1: {s}")

sizes = []
for point in low_points:
    sizes.append(size_basin([point]))
sizes.sort(reverse=True)

print(f"Part 2: {max(sizes) * max(sizes[1:]) * max(sizes[2:])}")