file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 6 Advent of Code Input.txt"

with open(file) as f:
    _, *times = f.readline().strip().split()
    _, *dists = f.readline().strip().split()
    times = list(map(int, times))
    dists = list(map(int, dists))

# counts = []
# for i, time in enumerate(times):
#     wins = 0
#     for t in range(time):
#         if t * (time - t) > dists[i]:
#             wins += 1
#     counts.append(wins)

# p = 1
# for c in counts:
#     p *= c

# print(p)
import math
# Part 2
times = list(map(str, times))
dists = list(map(str, dists))

time = int(''.join(times))
dist = int(''.join(dists))
print(f"{time=:,}")
print(f"{dist=:,}")
# time = 8
# dist = 10
count = time + 1
for t in range(time // 2):
    if t * (time - t) - dist < 0:
        count -= 2
    else:
        break
        # d = t * (time - t)
        # # midpoint = time // 2
        # # count = (midpoint - t) * 2
        # # break
        # # count += 1
        # print(f"{t=:,}")
        # print(f"{d=:,}")
        # # print(f"{count=:,}")
        # # break
print(f"{count:,}")

disc = math.sqrt(time**2 - 4 * dist)
t1 = (time - disc) / 2
t2 = (time + disc) / 2
print(f"{t1 = :,}")
print(f"{t2 = :,}")
print(f"{math.ceil(t1) = :,}")
print(f"{math.floor(t2) = :,}")
count = math.floor(t2) - math.ceil(t1) + 1
print(f"New count: {count:,}")
# 2a + 2b - 2a = 2b -> perimeter
# ab - a^2 = > area
# max area is when a = b / 2
# v * mobile_time - v * immobile_time
# a^2 = v * immobile_time