file = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2025 Day 7 Advent of Code Input.txt"

def advance_beam(grid, row=1, splits=0):
    if row + 1 == len(grid) - 1:
        for row in grid:
            print(''.join(row))
        return splits
    if row == 1:
        for col, ch in enumerate(grid[0]):
            if ch == 'S':
                grid[row][col] = '|'
                break
    for col, ch in enumerate(grid[row]):
        if ch == '|':
            if grid[row+1][col] == '^':
                splits += 1
                grid[row+1][col-1] = '|'
                grid[row+1][col+1] = '|'
            else:
                grid[row+1][col] = '|'
    row += 1
    return advance_beam(grid, row, splits)

# def advance_beam_2(grid_dict, row=0, timelines=0):
#     if row + 1 == len(grid) - 1:
#         # for row in grid:
#         #     print(''.join(row))
#         return timelines
#     if row == 0:
#         for key in grid_dict.keys():
#             if 'S' in grid_dict[key]:
#                 r, c = key
#                 grid_dict[(r+1, c)].append('|')
#                 break
#     for key in grid_dict.keys():
#         if '|' in grid_dict[key]:
#             r, c = key
#             if r < max(i for i, j in grid_dict.keys()) - 1:
#                 if '^' in grid_dict[(r+1, c)]:
#                     timelines += 2
#                     grid_dict[(r+1, c-1)].append('|')
#                     grid_dict[(r+1, c+1)].append('|')
#                 else:
#                     grid_dict[(r+1, c)].append('|')
#     row += 1
#     return advance_beam_2(grid_dict, row, timelines)

def build_grid():
    with open(file, 'rt') as f:
        new_grid = [[ch for ch in line.strip()] for line in f.readlines()]
    return new_grid   

def build_timelines(grid, steps=[], timelines=set(), switch=False, last_step_on_last_row=0, runs=0):
    if runs == 100:
        return len(timelines)
    initial_state = build_grid()
    # if runs == 1:
    #     print("Initial State")
    #     for row in grid:
    #         print(''.join(row))
    #     return 0
    for col, ch in enumerate(grid[0]):
        if ch == 'S':
            grid[1][col] = '|'
    row = 1
    d = (-1, 1)
    if switch:
        direction = d[1]
        switch = False
    else:
        direction = d[0]
        switch = True
    if len(steps) == 13:
        if steps[-1] != 0:
            last_step_on_last_row += 1
            # print(f"Before anything row = {row}")
            for i in range(len(steps)):
                for col, ch in enumerate(grid[row+i]):
                    if ch == '|':
                        if i == len(steps) - 1:
                            grid[row+1+i][col + steps[i] * -1] = '|'
                            break
                        else:
                            try:
                                grid[row+1+i][col + steps[i]] = '|'
                                break
                            except:
                                print(f'Row = {row}')
                                print(f"index = {i}")
                                break
            steps[-1] *= -1
            timelines.add(tuple(steps))
            for i in range(len(steps) - 3, -1, -1):
                if i != 0:
                    steps = steps[:i+1]
                    runs += 1
                    return build_timelines(initial_state, steps, timelines, switch, last_step_on_last_row, runs)
        else:
            last_step_i = [i for i in enumerate(steps, -len(steps)) if i != 0]
            for i in range(len(steps) - 2, -1, -1):
                if i != 0:
                    steps = steps[:i+1]
                    runs += 1
                    return build_timelines(initial_state, steps, timelines, switch, last_step_on_last_row, runs)
        
    if 0 < len(steps) < 13:
        for i in range(len(steps)):
            try:
                for col, ch in enumerate(grid[row+i]):
                    if ch == '|':
                        if i == len(steps) - 1:
                            grid[row+1+i][col + steps[i] * -1] = '|'
                            steps[i] = steps[i] * -1
                            break
                        else:
                            grid[row+1+i][col + steps[i]] = '|'
                            break
            except:
                print(f"{i=}")
                print(f"{row+i=}")
                return 0
        row += len(steps)
        while row < len(grid) - 2:
            for col, ch in enumerate(grid[row]):
                if ch == '|':
                    if grid[row+1][col] == '^':
                        grid[row+1][col+direction] = '|'
                        steps.append(direction)
                    else:
                        grid[row+1][col] = '|'
                        steps.append(0)
            row += 1

    if len(steps) == 0:
        while row < len(grid) - 2:
            for col, ch in enumerate(grid[row]):
                if ch == '|':
                    if grid[row+1][col] == '^':
                        grid[row+1][col+direction] = '|'
                        steps.append(direction)
                    else:
                        grid[row+1][col] = '|'
                        steps.append(0)
            row += 1
    if steps[-1] != 0:
        last_step_on_last_row += 1
    print('all finished')
    timelines.add(tuple(steps))
    for row in grid:
        print(''.join(row))
    runs += 1
    return build_timelines(initial_state, steps, timelines, switch, last_step_on_last_row, runs)

with open(file, 'rt') as f:
    matrix = [[ch for ch in line.strip()] for line in f.readlines()]
    
# timelines = set()
# # timelines.append(build_timeline(grid))
# steps_to_function = []
# # print(build_timeline(grid, steps=[-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1]))
# final_branch = False
# runs = 0
# steps_from_function = build_timelines(grid, steps_to_function)

# timelines.add(steps_from_function)

# steps_to_function = list(steps_from_function)

# while True:
#     if tuple(steps_to_function) in timelines:
#         steps_to_function[-1] *= -1
#         if tuple(steps_to_function) in timelines:
#             steps_to_function = steps_to_function[:-2]
#             steps_to_function[-1] *= -1
#             steps_to_function = list(build_timelines(grid, steps_to_function))
#         for i in range(len(steps_to_function) - 1, -1, -1):
#             steps_to_function = steps_to_function[:i+1]
#             steps_from_function = build_timelines(grid, steps_to_function)
#             steps_to_function = list(steps_from_function)
#             if steps_to_function in timelines:
                
# while runs < 100:
#     print(runs)
#     while tuple(steps_to_function) in timelines:
#         if final_branch:
#             final_branch = False
#             break
#         for i in range(-1, -len(steps_to_function) - 1, -1):
#             if steps_to_function[i] != 0:
#                 if i != -1:
#                     steps_to_function = steps_to_function[:i+1]
#                     steps_to_function[-1] *= -1
#                     steps_to_function = list(build_timeline(grid, steps_to_function))
#                 else:
#                     steps_to_function[i] *= -1
#                     timelines.add(steps_to_function)
#                     final_split = True
#                     break
#             if tuple(steps_to_function) not in timelines:
#                 timelines.add(steps_to_function)
#                 break
#             else:
#                 continue
#     runs += 1
arg_matrix = matrix[:]
print(build_timelines(arg_matrix))