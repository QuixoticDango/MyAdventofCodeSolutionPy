filename = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2017 Day 2 Advent of Code Input.txt"
with open(filename) as f:
    rows = [list(map(int, line.strip().split())) for line in f.readlines()]

# Part 1
checksum = sum(max(r) - min(r) for r in rows)
print(checksum)

# Part 2
for r in rows:
    r.sort(reverse=True)

checksum2 = 0
for r in rows:
    for k,n in enumerate(r):
        for i in range(r.index(n), len(r)):
            if n % r[i] == 0 and i != k:
                checksum2 += n // r[i]
checksum2_2 = sum(n // r[i] for r in rows for n in r for i in range(r.index(n) + 1, len(r)) if n % r[i] == 0)
print(checksum2, checksum2_2)