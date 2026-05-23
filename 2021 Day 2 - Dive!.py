filename = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 2 Advent of Code Input.txt"

with open(filename) as f:
    curr_pos = [0,0]
    curr_pos_2 = [0,0,0]
    for line in f.readlines():
        d, steps = line.strip().split()
        steps = int(steps)
        if d == "forward":
            curr_pos[1] += steps
            curr_pos_2[1] += steps
            curr_pos_2[0] += curr_pos_2[2] * steps
        if d == "down":
            curr_pos[0] += steps
            curr_pos_2[2] += steps
        if d == "up":
            curr_pos[0] -= steps
            curr_pos_2[2] -= steps
print(f"Part 1: {curr_pos[0] * curr_pos[1]}")
print(f"Part 2: {curr_pos_2[0] * curr_pos_2[1]}")