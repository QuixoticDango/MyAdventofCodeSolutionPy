import re
from copy import deepcopy

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 5 Advent of Code Input.txt"

with open(file) as f:
    stack_rows = []
    instructions = []
    stack_row = True
    for line in f.readlines():
        if stack_row:
            if line != '\n':
                stack_rows.append(line)
        else:
            instructions.append(line.strip())
        if line == '\n':
            stack_row = False

idxs = [stack_rows[-1].index(ch) for ch in stack_rows[-1] if ch.isnumeric()]
labels = [int(ch) for ch in stack_rows[-1] if ch.isnumeric()]
stacks = dict(zip(labels, [[] for l in labels]))

for line in reversed(stack_rows[:-1]):
    for i, ch in enumerate(line):
        if ch.isalpha():
            stacks[idxs.index(i)+1].append(ch)

print(instructions[0])
original_stacks = deepcopy(stacks)
print(f"{original_stacks = }")
for inst in instructions:
    m = tuple(map(int, re.search(r"move (\d+) from (\d+) to (\d+)", inst).group(1, 2, 3)))
    # stacks[m[2]].extend(stacks[m[1]][-1:-m[0]-1:-1])
    # stacks[m[1]] = stacks[m[1]][:-m[0]]
    count = m[0]
    lst = []
    while count > 0:
        box = stacks[m[1]].pop()
        box_2 = original_stacks[m[1]].pop()
        stacks[m[2]].append(box)
        count -= 1
        lst.append(box_2)
    
    original_stacks[m[2]].extend(reversed(lst))

tops = ''.join(v[-1] for k, v in stacks.items())
tops_2 = ''.join(v[-1] for k, v in original_stacks.items() if v)
print(f"Part 1: {tops}")
print(f"Part 2: {tops_2}")