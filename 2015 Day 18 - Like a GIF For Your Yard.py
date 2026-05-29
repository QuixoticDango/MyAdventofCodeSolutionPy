def animateGrid(grid, steps):
    if steps == 0:
        return grid
    
    alwaysOn = [(0,0), (0,99), (99,0),(99,99)]
    sumList = []
    for r,row in enumerate(grid):
        for c,col in enumerate(row):
            s = 0
            for i in range(3):
                for j in range(3):
                    try:
                        if grid[(r - 1) + i][(c - 1) + j] == '#' and not (i == 1 and j == 1):
                            if (r - 1) + i < 0 or (c - 1) + j < 0:
                                raise IndexError
                            s += 1
                    except IndexError:
                        pass
            sumList.append((r,c,s))
    for row, col, s in sumList:
        if (row,col) in alwaysOn:
                continue
        if grid[row][col] == '.' and s == 3:
            grid[row] = grid[row][:col] + '#' + grid[row][col+1:]
        if grid[row][col] == '#' and not (s == 2 or s == 3):
            grid[row] = grid[row][:col] + '.' + grid[row][col+1:]

    return animateGrid(grid, steps - 1)

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 18 Advent of Code Input.txt"
with open(filePath) as f:
    lightGrid = [line.strip() for line in f.readlines()]

for row in lightGrid:
    print(row)
print()

# animateGrid(lightGrid, 4)
count = sum(1 for row in animateGrid(lightGrid, 100) for ch in row if ch == '#')

for row in animateGrid(lightGrid, 100):
    print(row)
print()
print(count)

# for row in lightGrid
#     print(row)
# print()

# s = 0
# loopCount = 0
# for i in range(3):
#     for j in range(3):
#         loopCount += 1
#         try:
#             if lightGrid[(0 - 1) + i][(4 - 1) + j] == '#' and not (i == 1 and j == 1):
#                 if (0 - 1) + i < 0 or (4 - 1) + j < 0:
#                     raise IndexError
#                 s += 1
#         except IndexError:
#             pass
# print(f"{s=}")
# print(f"{loopCount=}")