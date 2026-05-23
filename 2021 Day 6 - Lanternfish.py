from collections import defaultdict

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 6 Advent of Code Input.txt"

with open(file) as f:
    lantern_fish = defaultdict(int)
    for fish in map(int, f.readline().strip().split(',')):
        lantern_fish[fish] += 1

days = 0
storage = 0
# Part 1: 80 days. Part 2: 256 days.
while days < 256:
    for i, fish in enumerate(sorted(lantern_fish)):
        if fish == 0:
            storage = lantern_fish[0]
            lantern_fish[0] = 0
        if fish > 0:
            lantern_fish[fish-1] = lantern_fish[fish]
            lantern_fish[fish] = 0
    else:
        if storage:
            lantern_fish[8] = storage
            lantern_fish[6] += storage
        storage = 0
    days += 1
print(f"Part 1: {sum(val for key, val in lantern_fish.items())}")