
filename = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2017 Day 8 Advent of Code Input.txt"

with open(filename) as f:
    lines = [line.strip().split() for line in f.readlines()]
    keys = [line[0] for line in lines]
    values = [line[1:] for line in lines]
    for i, vals in enumerate(values):
        for j, v in enumerate(vals):

            if v.isnumeric():
                values[i][values[i].index(vals[j])] = int(v)
    registers = {key:0 for key in keys}
    # print(f"{len(keys)=} and {len(values)=}")
    # print(lines)

maxReg2 = 0
for register, direction, amount, _, conditionReg, comparator, num in lines:
    if direction == 'inc':    
        if comparator == '>':
            if registers[conditionReg] > int(num):
                registers[register] += int(amount)
        if comparator == '<':
            if registers[conditionReg] < int(num):
                registers[register] += int(amount)
        if comparator == '>=':
            if registers[conditionReg] >= int(num):
                registers[register] += int(amount)
        if comparator == '<=':
            if registers[conditionReg] <= int(num):
                registers[register] += int(amount)
        if comparator == '==':
            if registers[conditionReg] == int(num):
                registers[register] += int(amount)
        if comparator == '!=':
            if registers[conditionReg] != int(num):
                registers[register] += int(amount)

    if direction == 'dec':    
        if comparator == '>':
            if registers[conditionReg] > int(num):
                registers[register] -= int(amount)
        if comparator == '<':
            if registers[conditionReg] < int(num):
                registers[register] -= int(amount)
        if comparator == '>=':
            if registers[conditionReg] >= int(num):
                registers[register] -= int(amount)
        if comparator == '<=':
            if registers[conditionReg] <= int(num):
                registers[register] -= int(amount)
        if comparator == '==':
            if registers[conditionReg] == int(num):
                registers[register] -= int(amount)
        if comparator == '!=':
            if registers[conditionReg] != int(num):
                registers[register] -= int(amount)
    currentMax = max(registers[reg] for reg in registers)
    if currentMax > maxReg2:
        maxReg2 = currentMax


maxReg = max(registers[reg] for reg in registers)

print(f"Part 1: {maxReg=}")
print(f"Part 2: {maxReg2=}")