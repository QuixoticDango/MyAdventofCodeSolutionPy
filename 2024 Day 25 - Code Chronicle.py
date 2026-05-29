file_path = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2024 Day 25 Advent of Code Input.txt"
lines = []
with open(file_path, "r") as file:
    for line in file.readlines():
        if line != '\n':
            lines.append(line.strip())

locks = [['' for j in range(7)] for i in range(250)]
keys = [['' for j in range(7)] for i in range(250)]
lock_count = 0
key_count = 0
for i in range(500):
    for j in range(7):
        if lines[0 + 7 * i] == '#####':
            locks[lock_count][j] = lines[j + 7 * i]
            lock_count += j // 6
        if lines[0 + 7 * i] == '.....':
            keys[key_count][j] = lines[j + 7 * i]
            key_count += j // 6

def doesKeyMatchLock(locks, keys):
    lock_heights = [[0 for j in range(5)] for i in range(len(locks))]
    key_heights = [[0 for j in range(5)] for i in range(len(keys))]
    lock_row = 0
    key_row = 0

    for lock in locks:
        for col in range(5):
            for row in range(7):
                if lock[row][col] == '#':
                    lock_heights[lock_row][col] += 1
        lock_row += 1

    for key in keys:
        for col in range(5):
            for row in range(7):
                if key[row][col] == '#':
                    key_heights[key_row][col] += 1
        key_row += 1
    
    sum = 0
    lockKeyPairs = []
    for l in lock_heights:
        for k in key_heights:
            if all([l[i] + k[i] <= 7 for i in range(5)]):
                sum += 1
                lockKeyPairs.append((l,k))
    return lockKeyPairs

print(len(doesKeyMatchLock(locks, keys)))