file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 1 Advent of Code Input.txt"

with open(file) as f:
    depth = [int(line.strip()) for line in f.readlines()]
print(f"Part 1: {sum(1 for i, n in enumerate(depth) if i > 0 and n > depth[i-1])}")
print(f"Part 2: {sum(1 for i, n in enumerate(depth)
                     if 0 < i < len(depth)-1 and sum(depth[j] for j in range(i-1, i+2)) > \
                        sum(depth[j] for j in range(i-2, i+1)))}")
