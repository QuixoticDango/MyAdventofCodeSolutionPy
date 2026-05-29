from itertools import product

def flash(g: list[list[int]], points: list[tuple[int, int]]) -> int:
    for point in points:
        i, j = point
        g[i][j] = 0
        for d in directions:
            if not (0 <= i+d[0] < len(g) and 0 <= j+d[1] < len(g[0])):
                continue
            if (i+d[0], j+d[1]) not in points:
                g[i+d[0]][j+d[1]] += 1
                if g[i+d[0]][j+d[1]] > 9:
                    points.append((i+d[0], j+d[1]))
    return len(points)

def charge_octopi(g: list[list[int]], flashes: int = 0, count: int = 0) -> int:
    ready_to_flash = []
    if count == 100:
        return flashes
    for i, row in enumerate(g):
        for j, charge in enumerate(row):
            if charge < 9:
                g[i][j] += 1
            else:
                ready_to_flash.append((i,j))
    if ready_to_flash:
        flashes += flash(g, ready_to_flash)
    return charge_octopi(g, flashes, count=count+1)

def final_flash(g: list[list[int]], flashes: int = 0, count: int = 0) -> int:
    ready_to_flash = []
    for i, row in enumerate(g):
        for j, charge in enumerate(row):
            if charge < 9:
                g[i][j] += 1
            else:
                ready_to_flash.append((i,j))
    if ready_to_flash:
        flashes += flash(g, ready_to_flash)
    if all(n == 0 for row in g for n in row):
        return count + 1
    return final_flash(g, flashes, count=count+1)

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 11 Advent of Code Input.txt"

with open(file) as f:
    grid = [[int(ch) for ch in line.strip()] for line in f.readlines()]
directions = tuple(product((-1,0,1), repeat=2))
grid_1 = [row[:] for row in grid]
grid_2 = [row[:] for row in grid]
print(f"Part 1: {charge_octopi(grid_1)}")
print(f"Part 2: {final_flash(grid_2)}")

# def solve_dumbo_octopus(grid):
#     def step(g):
#         # Increment all
#         for i in range(10):
#             for j in range(10):
#                 g[i][j] += 1

#         flashed = set()
#         queue = [(i, j) for i in range(10) for j in range(10) if g[i][j] > 9]

#         while queue:
#             i, j = queue.pop()
#             if (i, j) in flashed:
#                 continue
#             flashed.add((i, j))
#             for di in (-1, 0, 1):
#                 for dj in (-1, 0, 1):
#                     ni, nj = i + di, j + dj
#                     if 0 <= ni < 10 and 0 <= nj < 10 and (ni, nj) not in flashed:
#                         g[ni][nj] += 1
#                         if g[ni][nj] > 9:
#                             queue.append((ni, nj))

#         # Reset flashed octopuses
#         for i, j in flashed:
#             g[i][j] = 0

#         return len(flashed)

#     total_flashes = 0
#     part1 = None
#     part2 = None

#     for step_num in range(1, 1000):
#         flashes = step(grid)
#         if step_num <= 100:
#             total_flashes += flashes
#         if step_num == 100:
#             part1 = total_flashes
#         if flashes == 100:  # All flashed
#             part2 = step_num
#             break

#     print(f"Part 1: {part1}")
#     print(f"Part 2: {part2}")

# # Run with input
# with open(r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 11 Advent of Code Input.txt") as f:
#     grid = [[int(c) for c in line.strip()] for line in f]
# solve_dumbo_octopus(grid)   