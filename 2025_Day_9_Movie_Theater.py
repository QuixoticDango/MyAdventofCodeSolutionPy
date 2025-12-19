import math

def build_grid(red_points):
    max_row = max(p[1] + 1 for p in red_points) + 2
    max_col = max(p[0] + 1 for p in red_points) + 2
    min_row = min(p[1] for p in red_points)
    min_col = min(p[0] for p in red_points if p[1] == min_row)
    next_point_col = min(p[0] for p in red_points if p[0] != min_col and p[1] == min_row)
    next_point_row = [p[1] for p in red_points if p[0] == next_point_col][0]
    return (min_col, min_row, next_point_col, next_point_row)

    # grid = [['#' if (j, i) in red_points else '.' for j in range(max_col)] for i in range(max_row)]
    # for row in grid:
    #     print(''.join(row))

file = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2025 Day 9 Advent of Code Input.txt"

with open(file, 'rt') as f:
    points = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

max_area = max((abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
               for i, p1 in enumerate(points)
               for j, p2 in enumerate(points)
               if i != j and p1[0] != p2[0] and p1[1] != p2[1])
print(max_area)

print(build_grid(points))