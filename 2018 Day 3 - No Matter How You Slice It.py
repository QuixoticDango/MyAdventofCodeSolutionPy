file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2018 Day 3 Advent of Code Input.txt"

stream = open(file, 'rt')
claims = {line.strip().split('@')[0].strip():[line.strip().split('@')[1].strip()]
          for line in stream.readlines()}
stream.close()

# Part 1
for key in claims.keys():
    claims[key] = claims[key][0].split(':')
    claims[key] = list(map(int, claims[key][0].split(','))) + list(map(int, claims[key][1].split('x')))

max_width = max(claims[key][0] + claims[key][2] for key in claims.keys())
max_height = max(claims[key][1] + claims[key][3] for key in claims.keys())

grid = {(i, j):[] for j in range(max_width) for i in range(max_height)}

for key in claims.keys():
    col, row, w, h = claims[key]
    for i in range(row, row + h):
        for j in range(col, col + w):
            grid[(i, j)].append('.')
            if len(grid[(i, j)]) > 1:
                continue

overlapping_area = 0
for key in grid.keys():
    if len(grid[key]) > 1:
        overlapping_area += 1
print(overlapping_area)

# Part 2

# is_overlapping = False
overlapped_rectangles = []
for key1 in claims.keys():
    if key1 in overlapped_rectangles:
        continue
    for key2 in claims.keys():
        if key1 == key2:
            continue
        col1, row1, w1, h1 = claims[key1]
        col2, row2, w2, h2 = claims[key2]
        # points1 = [(i, j) for i in range(row1, row1 + h1) for j in range(col1, col1 + w1)]
        # points2 = [(h, k) for h in range(row2, row2 + h2) for k in range(col2, col2 + w2)]
        # if any((i, j) == (h, k)
        #        for i in range(row1, row1 + h1)
        #        for j in range(col1, col1 + w1)
        #        for h in range(row2, row2 + h2)
        #        for k in range(col2, col2 + w2)):
        if any(row1 <= h <= row1 + h1 and col1 <= k <= col1 + w1
               for h in range(row2, row2 + h2)
               for k in range(col2, col2 + w2)):
            
            overlapped_rectangles.append(key1)
            overlapped_rectangles.append(key2)
            break

print([key for key in claims.keys() if key not in overlapped_rectangles][0])