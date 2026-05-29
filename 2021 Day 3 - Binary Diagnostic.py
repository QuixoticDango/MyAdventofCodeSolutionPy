filename = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 3 Advent of Code Input.txt"

with open(filename) as f:
    lines = [line.strip() for line in f.readlines()]
    for i, line in enumerate(lines):
        if i == 0:
            digit_counts = [{'0':0, '1':0} for i in range(len(line))]
        for j, ch in enumerate(line):
            digit_counts[j][ch] += 1
gamma = int(''.join('0' if count['0'] > count['1'] else '1' for count in digit_counts), 2)
epsilon = int(''.join('0' if count['0'] < count['1'] else '1' for count in digit_counts), 2)
print(f"Part 1: {gamma * epsilon}")


discarded = set()
i = 0
all_done = False
check_digit = None
while i < len(lines[0]):
    remaining_lines = [line for line in lines if line not in discarded]
    if len(remaining_lines) == 2:
        oxygen = remaining_lines[0] if remaining_lines[0][i] == '1' else remaining_lines[1]
    if len(remaining_lines) == 1:
        oxygen = remaining_lines[0]
        break
    column = tuple(zip(*remaining_lines))[i]
    check_digit = '1' if 2 * column.count('1') >= len(column) else '0'
    for j, line in enumerate(lines):
        if line not in discarded:
            if line[i] != check_digit:
                discarded.add(line)
    i += 1

discarded = set()
i = 0
all_done = False
check_digit = None
while i < len(lines[0]):
    remaining_lines = [line for line in lines if line not in discarded]
    if len(remaining_lines) == 2:
        co2 = remaining_lines[0] if remaining_lines[0][i] == '0' else remaining_lines[1]
        break
    if len(remaining_lines) == 1:
        co2 = remaining_lines[0]
        break
    column = tuple(zip(*remaining_lines))[i]
    check_digit = '0' if 2 * column.count('0') <= len(column) else '1'
    for j, line in enumerate(lines):
        if line not in discarded:
            if line[i] != check_digit:
                discarded.add(line)
    i += 1

print(f"Part 2: {int(oxygen, 2) * int(co2, 2)}")