import time
start = time.time()
file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2018 Day 2 Advent of Code Input.txt"

with open(file, 'rt') as f:
    ids = [line.strip() for line in f.readlines()]

# Part 1
duos = 0
trios = 0
letter_dict = {id:[] for id in ids}
for i, id in enumerate(ids):
    for j in range(26):
        count = 0
        for ch in id:
            if ch == chr(ord('a') + j):
                count += 1
        if count == 3:
            letter_dict[id].append((chr(ord('a') + j), count))
        if count == 2:
            letter_dict[id].append((chr(ord('a') + j), count))

for id in letter_dict.keys():
    if any(count == 3 for ch, count in letter_dict[id]):
        trios += 1
    if any(count == 2 for ch, count in letter_dict[id]):
        duos += 1
print(duos * trios)

# Part 2

found = False
for i, id1 in enumerate(ids):
    if found:
        break
    for j, id2 in enumerate(ids):
        mismatch = 0
        if i == j:
            continue
        if len(id1) != len(id2):
            continue
        for k in range(len(id1)):
            if id1[k] != id2[k]:
                mismatch += 1
            if mismatch > 1:
                break
        if mismatch == 1:
            print(''.join([ch for c, ch in enumerate(id1) if ch == id2[c]]))
            found = True
            break
print(f"Runtime: {time.time() - start}")