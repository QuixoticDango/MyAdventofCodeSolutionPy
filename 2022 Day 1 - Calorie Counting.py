file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 1 Advent of Code Input.txt"

with open(file) as f:
    max_cals = -1
    elf = []
    elves = []
    line = f.readline()
    while line:
        if line == "\n":
            cals = sum(elf)
            elves.append(cals)
            elf = []
            if cals > max_cals:
                max_cals = cals
        else:
            elf.append(int(line.strip()))
        line = f.readline()
    else:
        cals = sum(elf)
        elves.append(cals)
        if cals > max_cals:
            max_cals = cals

print(f"Part 1: {max_cals}")

elves = sorted(elves, reverse=True)
top_three = elves[0] + elves[1] + elves[2]
print(f"Part 2: {top_three}")