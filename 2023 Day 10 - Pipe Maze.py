from itertools import product

class NegativeIndex(IndexError):
    pass

def change_direction(previous_direction, ch):
    if ch in "-|":
        return previous_direction
    if ch in "FJ":
        return (-previous_direction[1], -previous_direction[0])
    if ch in "L7":
        return (previous_direction[1], previous_direction[0])
    
file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 10 Advent of Code Input.txt"

with open(file) as f:
    pipe_grid = [line.strip() for line in f.readlines()]

bounds = {'row':(0, len(pipe_grid)), 'col':(0, len(pipe_grid[0]))}
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
can_be_entered_moving_up = set(["|", "F", "7", "S"])
can_be_entered_moving_down = set(["|", "L", "J", "S"])
can_be_entered_moving_left = set(["-", "F", "L", "S"])
can_be_entered_moving_right = set(["-", "J", "7", "S"])

all_pipe_segemnts = can_be_entered_moving_down | can_be_entered_moving_left | can_be_entered_moving_right | can_be_entered_moving_up
# print(all_pipe_segemnts)

loop_loc = set()

current_loc = None
for r, row in enumerate(pipe_grid):
    for c, ch in enumerate(row):
        if ch == 'S':
            current_loc = (r, c)
            loop_loc.add(current_loc)

loc_count = 1
i = 0
current_ch = None
for d in dir:
    new_loc = (current_loc[0] + d[0], current_loc[1] + d[1])
    new_row, new_col = new_loc
    if d[0] == 1 and pipe_grid[new_row][new_col] in can_be_entered_moving_down:
        current_loc = new_loc
        previous_dir = d
        current_ch = pipe_grid[new_row][new_col]
        loop_loc.add(new_loc)
        break
    if d[0] == -1 and pipe_grid[new_row][new_col] in can_be_entered_moving_up:
        current_loc = new_loc
        previous_dir = d
        current_ch = pipe_grid[new_row][new_col]
        loop_loc.add(new_loc)
        break
    if d[1] == 1 and pipe_grid[new_row][new_col] in can_be_entered_moving_right:
        current_loc = new_loc
        previous_dir = d
        current_ch = pipe_grid[new_row][new_col]
        loop_loc.add(new_loc)
        break
    if d[1] == -1 and pipe_grid[new_row][new_col] in can_be_entered_moving_left:
        current_loc = new_loc
        previous_dir = d
        current_ch = pipe_grid[new_row][new_col]
        loop_loc.add(new_loc)
        break

steps = 1
while current_ch != 'S':
    current_dir = change_direction(previous_dir, current_ch)
    new_loc = (current_loc[0] + current_dir[0], current_loc[1] + current_dir[1])
    loop_loc.add(new_loc)
    new_row, new_col = new_loc
    current_ch = pipe_grid[new_row][new_col]
    previous_dir = current_dir
    current_loc = new_loc
    steps += 1

print(steps)
print(f"Part 1: {steps // 2}")

# for row, col in loop_loc:
#     pipe_grid[row] = pipe_grid[row][:col] + 'X' + pipe_grid[row][col + 1:]

print('\n'.join(pipe_grid))
print()
# first_x_loc = None
# last_x_loc = None
countable_vertex_pairs = {"F":"J", "J":"F", "L":"7", "7":"L"}
total = 0
for r, row in enumerate(pipe_grid):
    inside_loop = False
    in_wall = False
    check = False
    for c, ch in enumerate(row):
        if (r,c) not in loop_loc:
            ray_cast_count = 0
            ray_check = ''
            for l,p in enumerate(row[c+1:], 1):
                if p in '|S' and (r, c+l) in loop_loc:
                    ray_cast_count += 1
                if p in "7JLF" and (r,c+l) in loop_loc:
                    ray_check += p
            b = 0
            if len(ray_check) >= 2:
                while b < len(ray_check):
                    try:
                        check = ray_check[b] + ray_check[b+1]
                        if check == "FJ" or check == "L7":
                            ray_cast_count += 1
                        b += 2
                    except IndexError:
                        break
            if ray_cast_count % 2 == 1:
                total += 1
                pipe_grid[r] = pipe_grid[r][:c] + 'I' + pipe_grid[r][c+1:]
            else:
                pipe_grid[r] = pipe_grid[r][:c] + 'O' + pipe_grid[r][c+1:]
print('\n'.join(pipe_grid))
print(total)