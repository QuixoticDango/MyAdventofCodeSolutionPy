file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 4 Advent of Code Input.txt"

with open(file) as f:
    count = 0
    count_2 = 0
    lines = f.read().splitlines()
    for line in lines:
        r1, r2 = line.split(',')
        r1 = tuple(map(int, r1.split('-')))
        r2 = tuple(map(int, r2.split('-')))
        
        r1 = set(i for i in range(r1[0], r1[1]+1))
        r2 = set(i for i in range(r2[0], r2[1]+1))

        if r1 & r2 == r1 or r1 & r2 == r2:
            count += 1

        if r1 & r2:
            count_2 += 1

print(f"Part 1: {count}")
print(f"Part 2: {count_2}")