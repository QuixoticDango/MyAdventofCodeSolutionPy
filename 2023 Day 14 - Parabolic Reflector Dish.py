from collections.abc import Iterable

def compute_load(g):
    load = 0
    for i, line in enumerate(g):
        for j, ch in enumerate(line):
            if ch == "O":
                load += len(g) - i
    return load

def tilt_focus(g):
    new_g = [row[:] for row in g]
    for i, row in enumerate(new_g):
        if i == 0:
            continue
        for j, ch in enumerate(row):
            if ch == 'O':
                for r in reversed(range(i)):
                    if new_g[r][j] in 'O#':
                        new_g[i][j] = '.'
                        new_g[r+1][j] = 'O'
                        break
                    if r == 0 and new_g[r][j] == '.':
                        new_g[i][j] = '.'
                        new_g[r][j] = 'O'
                        break
    return new_g

def tilt_north(g: Iterable):
    new_g = [row[:] for row in g]
    for i, row in enumerate(new_g):
        if i == 0:
            continue
        for j, ch in enumerate(row):
            if ch == 'O':
                for r in reversed(range(i)):
                    if new_g[r][j] in 'O#':
                        new_g[i][j] = '.'
                        new_g[r+1][j] = 'O'
                        break
                    if r == 0 and new_g[r][j] == '.':
                        new_g[i][j] = '.'
                        new_g[r][j] = 'O'
                        break
    return new_g
    
def tilt_west(g: Iterable):
    new_g = [row[:] for row in g]
    for i, row in enumerate(new_g):
        for j, ch in enumerate(row):
            if j == 0:
                continue
            if ch == 'O':
                for c in reversed(range(j)):
                    if new_g[i][c] in 'O#':
                        new_g[i][j] = '.'
                        new_g[i][c+1] = 'O'
                        break
                    if c == 0 and new_g[i][c] == '.':
                        new_g[i][j] = '.'
                        new_g[i][c] = 'O'
    return new_g

def tilt_south(g: Iterable):
    new_g = [row[:] for row in g]
    for i, row in reversed(tuple(enumerate(new_g))):
        for j, ch in enumerate(row):
            if i == len(g) - 1:
                continue
            if ch == 'O':
                for r in range(i+1, len(new_g)):
                        if new_g[r][j] in 'O#':
                            new_g[i][j] = '.'
                            new_g[r-1][j] = 'O'
                            break
                        if r == len(new_g) - 1 and new_g[r][j] == '.':
                            new_g[i][j] = '.'
                            new_g[r][j] = 'O'
                            break
    return new_g

def tilt_east(g: Iterable):
    new_g = [row[:] for row in g]
    for i, row in enumerate(new_g):
        for j, ch in reversed(tuple(enumerate(row))):
            if j == len(row) - 1:
                continue
            if ch == 'O':
                for c in range(j+1, len(row)):
                    if new_g[i][c] in 'O#':
                        new_g[i][j] = '.'
                        new_g[i][c-1] = 'O'
                        break
                    if c == len(row) - 1 and new_g[i][c] == '.':
                        new_g[i][j] = '.'
                        new_g[i][c] = 'O'
    return new_g

def cycle_stage(g: Iterable, history=None, seen=None, cycles: int = 0):
    if history is None:
        history = []
    if seen is None:
        seen = {}

    new_g = [row[:] for row in g]
    state = (tuple(tuple(row) for row in new_g))

    # if cycles == 0:
    #     history.append(state)
    #     seen[state] = cycles

    new_g = tilt_east(tilt_south(tilt_west(tilt_north(new_g))))
    cycles += 1

    if state in seen:
        loop_start = seen[state]
        loop_length = cycles - loop_start
        return history, loop_start, loop_length
    else:
        history.append(state)
        seen[state] = cycles

    return cycle_stage(new_g, history, seen, cycles)

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 14 Advent of Code Input.txt"

with open(file) as f:
    grid = [[ch for ch in line.strip()] for line in f.readlines()]

original_grid = [row[:] for row in grid]
grid = tilt_focus(grid)

print(f"Part 1: {compute_load(grid)}")

configs, start, length = cycle_stage(original_grid)
configs = configs[1:]
# print(f"{configs.index(configs[-1])=}")
idx = (1000000000 - start) % length
sol = configs[start + idx - 1]
print(f"Part 2: {compute_load(sol)}")