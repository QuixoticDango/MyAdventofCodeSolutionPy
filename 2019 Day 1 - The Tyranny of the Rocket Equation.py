file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2019 Day 1 Advent of Code Input.txt"

# Part 1
print(sum(map(lambda m: divmod(m, 3)[0] - 2, map(int, (line.strip() for line in open(file).readlines())))))

# Part 2
with open(file) as f:
    masses = list(map(int, (line.strip() for line in f.readlines())))

total_fuel = 0
for m in masses:
    fuel = 0
    while m > 0:
        m = divmod(m, 3)[0] - 2
        if m >= 0:
            fuel += m
    total_fuel += fuel

print(total_fuel)