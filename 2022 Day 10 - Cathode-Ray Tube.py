

file: str = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 10 Advent of Code Input.txt"

with open(file) as f:
    instructions = f.read().splitlines()
    instructions = [inst if inst == 'noop' else int(inst.split()[1])
                    for inst in instructions]

crt = [['.' for j in range(40)] for i in range(6)]
idx: int = 0
cycles: int = 1
x: int = 1
num_to_add: int = 0
addx_found: bool = False
checksum: int = 0
curr_pixel = 0
while idx < len(instructions):
    if curr_pixel % 40 in [x-1, x, x+1]:
            crt[curr_pixel // 40][curr_pixel % 40] = "#"
    if addx_found:
        x += num_to_add
        addx_found = False
        cycles += 1
        idx += 1
        curr_pixel += 1
        if cycles in set(i for i in range(20, 260, 40)):
            checksum += cycles * x
        continue
    if type(instructions[idx]) == int:
        addx_found = True
        num_to_add = instructions[idx]
    if instructions[idx] == 'noop':
        idx += 1
    cycles += 1
    curr_pixel += 1
    if cycles in set(i for i in range(20, 260, 40)):
        checksum += cycles * x
print(f"Part 1: {checksum}")
print("Part 2:")
print("========================================")
print('\n'.join(''.join(ch for ch in row) for row in crt))