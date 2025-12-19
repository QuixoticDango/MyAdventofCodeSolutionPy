file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2018 Day 1 Advent of Code Input.txt"

with open(file, 'rt') as f:
    changes = [int(line.strip()[1:]) if line[0] == '+' else -int(line.strip()[1:])
         for line in f.readlines()]

frequency = 0
for f in changes:
    frequency += f
print(frequency)

# Part 2
frequencies = [0]
frequency = 0
duplicate_found = False
while True:
    if duplicate_found:
        break
    for f in changes:
        frequency += f
        if frequency in frequencies:
            duplicate_found = True
            break
        frequencies.append(frequency)
print(frequency)