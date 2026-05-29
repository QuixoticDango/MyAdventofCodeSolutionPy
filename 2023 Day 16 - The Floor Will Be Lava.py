from collections import defaultdict
from itertools import product
from copy import deepcopy

class NegativeIndex(IndexError):
    pass

def in_bounds(laser):
    if not (0 <= laser[0] < length and 0 <= laser[1] < width):
        return False
    return True

def hit_wall(laser, grid):
    if (laser[0] == 0 or laser[0] == length - 1 or laser[1] == 0 or laser[1] == width - 1)\
        and grid[(laser[0], laser[1])] == '.':
        return True
    return False

def propagate_laser(grid: dict, l: int, w: int, laser_pos: list = [(0, 0, 0, set())]):
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    d_dict = {"\\":{0:1, 1:0, 2:3, 3:2}, "/":{0:3, 3:0, 1:2, 2:1}}
    counts = 0
    while laser_pos:
        try:
            for n, pos in enumerate(laser_pos):
                if pos[0] < 0 or pos[1] < 0:
                    raise NegativeIndex
                # print(f"{pos = }")
                # print(f"{len(pos) = }")
                i, j, d, se = pos
                # print(f"what {se = }")

                if (i,j,d) in se:
                    # print(f"{len(laser_pos) = }")
                    # print(f"{n = }")
                    del laser_pos[n]
                    continue

                se.add((i,j,d))

                if "#" not in grid[(i,j)]:
                    grid[(i,j)].append('#')

                if '.' in grid[(i,j)]:
                    laser_pos[n] = (i + direction[d][0], j + direction[d][1], d, se)
                    continue

                if "\\" in grid[(i,j)]:
                    d = d_dict[grid[(i,j)][0]][d]
                    laser_pos[n] = (i + direction[d][0], j + direction[d][1], d, se)
                    continue

                if "/" in grid[(i,j)]:
                    # print('FORWARD SLASH!')
                    # print(f"{d=}")
                    # print(f"{d_dict[grid[(i,j)][0]][d]=}")
                    d = d_dict[grid[(i,j)][0]][d]
                    laser_pos[n] = (i + direction[d][0], j + direction[d][1], d, se)
                    continue

                if "-" in grid[(i,j)] and d % 2 == 0:
                    laser_pos[n] = (i + direction[d][0], j + direction[d][1], d, se)
                    continue
                
                if "-" in grid[(i,j)] and d % 2 == 1:
                    d_split = [i for i in range(4) if i % 2 == 0]
                    laser_pos.append((i + direction[d_split[0]][0], j + direction[d_split[0]][1], d_split[0], se))
                    laser_pos[n] = (i + direction[d_split[1]][0], j + direction[d_split[1]][0], d_split[1], se)
                    continue

                if "|" in grid[(i,j)] and d % 2 == 1:
                    laser_pos[n] = (i + direction[d][0], j + direction[d][1], d, se)
                    continue

                if "|" in grid[(i,j)] and d % 2 == 0:
                    d_split = [i for i in range(4) if i % 2 == 1]
                    laser_pos.append((i + direction[d_split[0]][0], j + direction[d_split[0]][1], d_split[0], se))
                    laser_pos[n] = (i + direction[d_split[1]][0], j + direction[d_split[1]][1], d_split[1], se)
                    continue
                
                if not in_bounds(laser_pos[n]) or hit_wall(laser_pos[n], grid):
                    del laser_pos[n]
        except NegativeIndex:
            # print(f"{laser_pos = }")
            # print(f"{n = }")
            if laser_pos:
                del laser_pos[n]
            else:
                break
        counts += 1
        # new_grid = dict()
        # for a, b in grid:
        #     if 0 <= a < l and 0 <= b < w:
        #         # print(a)
        #         new_grid[(a,b)] = grid[(i,j)]
    return grid

def propagate_laser_2(grid: dict, l: int, w: int, laser_pos: list = [(0, 0, 0, set())]):
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    d_dict = {"\\":{0:1, 1:0, 2:3, 3:2}, "/":{0:3, 3:0, 1:2, 2:1}}
    counts = 0
    visited_sites = set()
    delete_these = []
    start = deepcopy(laser_pos)
    while laser_pos:
        try:
            n = 0
            while n < len(laser_pos):
                pos = laser_pos[n]

                if pos[0] < 0 or pos[1] < 0:
                    raise NegativeIndex
                i, j, d, se = pos

                if (i,j,d) in se:
                    # del laser_pos[n]
                    delete_these.append(laser_pos[n])
                    laser_pos = [l_pos for l_pos in laser_pos if l_pos not in delete_these]
                    continue

                se.add((i,j,d))
                visited_sites.add((i,j))

                if '.' in grid[(i,j)]:
                    laser_pos[n] = (i + direction[d][0], j + direction[d][1], d, se)
                    continue

                if "\\" in grid[(i,j)]:
                    d = d_dict[grid[(i,j)][0]][d]
                    laser_pos[n] = (i + direction[d][0], j + direction[d][1], d, se)
                    continue

                if "/" in grid[(i,j)]:
                    d = d_dict[grid[(i,j)][0]][d]
                    laser_pos[n] = (i + direction[d][0], j + direction[d][1], d, se)
                    continue

                if "-" in grid[(i,j)] and d % 2 == 0:
                    laser_pos[n] = (i + direction[d][0], j + direction[d][1], d, se)
                    continue
                
                if "-" in grid[(i,j)] and d % 2 == 1:
                    d_split = [i for i in range(4) if i % 2 == 0]
                    laser_pos.append((i + direction[d_split[0]][0], j + direction[d_split[0]][1], d_split[0], se.copy()))
                    laser_pos[n] = (i + direction[d_split[1]][0], j + direction[d_split[1]][0], d_split[1], se.copy())
                    continue

                if "|" in grid[(i,j)] and d % 2 == 1:
                    laser_pos[n] = (i + direction[d][0], j + direction[d][1], d, se)
                    continue

                if "|" in grid[(i,j)] and d % 2 == 0:
                    d_split = [i for i in range(4) if i % 2 == 1]
                    laser_pos.append((i + direction[d_split[0]][0], j + direction[d_split[0]][1], d_split[0], se.copy()))
                    laser_pos[n] = (i + direction[d_split[1]][0], j + direction[d_split[1]][1], d_split[1], se.copy())
                    continue
                
                if not in_bounds(laser_pos[n]) or hit_wall(laser_pos[n], grid):
                    # del laser_pos[n]
                    delete_these.append(laser_pos[n])
        except NegativeIndex:
            if laser_pos:
                delete_these.append(laser_pos[n])
            else:
                break
        laser_pos = [l_pos for l_pos in laser_pos if l_pos not in delete_these]
        print(f"{start = }")
        print(f"{len(laser_pos) = }")
        print()
        counts += 1
    return len(visited_sites)

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 16 Advent of Code Input.txt"

with open(file) as f:
    light_grid = defaultdict(list)
    length = 0
    width = 0
    for i, line in enumerate(f.readlines()):
        length = i + 1
        for j, ch in enumerate(line.strip()):
            width = j + 1
            light_grid[(i,j)].append(ch)

original_light_grid = deepcopy(light_grid)
propagate_laser(light_grid, length, width)
grid = [['' for j in range(width)] for i in range(length)]
new_dict = dict()
for pos in light_grid:
    if not (0 <= pos[0] < length and 0 <= pos[1] < width):
        continue
    else:
        new_dict[pos] = light_grid[pos]
    if pos not in tuple(product([j for j in range(110)], repeat=2)):
        print(f"offender {pos}")
    if light_grid[pos] == []:
        print(f"empty list {pos}")
    try:
        grid[pos[0]][pos[1]] += light_grid[pos][0] if "#" not in light_grid[pos] else "#"
    except IndexError:
        print(f"Index Error: {pos}")
print('\n'.join(''.join(ch for ch in row) for row in grid))
checksum = sum(1 for pos in new_dict if "#" in new_dict[pos])
print(f"Part 1: {checksum}")

# Part 2
corners = [[(0,0,0,set())],[(0,0,1, set())], [(0,width-1,1, set())], [(0,width-1,2, set())],
           [(length-1,0,0, set())], [(length-1,0,3, set())],
           [(length-1,width-1,2, set())], [(length-1,width-1,3,set())]]
starting_points = [[(i, j, d, set())]
                   for i in range(length)
                   for j in range(width)
                   for d in range(4)
                   if (i == 0 and d == 1\
                    or j == 0 and d == 0\
                        or i == length-1 and d == 3\
                            or j == width-1 and d == 2)\
                                and (i,j,d) not in corners]
all_starts = corners + starting_points
print(f"Part 2: {max(propagate_laser_2(original_light_grid, length, width, start) for start in all_starts)}")