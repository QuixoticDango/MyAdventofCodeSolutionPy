def createGrid(num):
    d = [(0,1), (-1,0), (0,-1), (1,0)]
    s = 1
    while s**2 < num:
        s += 2

    gridLength = s

    grid = [[0 for cols in range(gridLength)] for rows in range(gridLength)]

    initPos = (gridLength // 2, gridLength // 2)
    
    data = 1
    direction = 0
    steps = 0
    stepCount = 0
    newPos = initPos
    while data <= num:

        if direction % 2 == 0:
            stepCount += 1
        steps = stepCount
        stepDirection = d[direction % 4]

        while steps > 0 and data <= num:
            grid[newPos[0]][newPos[1]] = data
            newPos = (newPos[0] + stepDirection[0], newPos[1] + stepDirection[1])
            data += 1
            steps -= 1

        direction += 1

    # rowStr = [list(map(str, row)) for row in grid]
    # for row in rowStr:
    #     for ch in row:
    #         spaces = ' ' * (6 - len(ch))
    #         print(spaces + ch, end='')
    #     print()

    return grid

def createGrid2(num):
    d = [(0,1), (-1,0), (0,-1), (1,0)]
    s = 1
    while s**2 < num:
        s += 2

    gridLength = s

    grid = [[0 for cols in range(gridLength)] for rows in range(gridLength)]

    initPos = (gridLength // 2, gridLength // 2)
    
    data = 1
    direction = 0
    steps = 0
    stepCount = 0
    newPos = initPos
    check = False
    while True:
        if check == True:
            break
        if direction % 2 == 0:
            stepCount += 1
        steps = stepCount
        stepDirection = d[direction % 4]

        while steps > 0:
            grid[newPos[0]][newPos[1]] = data
            newPos = (newPos[0] + stepDirection[0], newPos[1] + stepDirection[1])
            data = grid[newPos[0] - 1][newPos[1]] + grid[newPos[0] - 1][newPos[1] - 1] + grid[newPos[0]][newPos[1] - 1] \
            + grid[newPos[0] + 1][newPos[1] - 1] + grid[newPos[0] + 1][newPos[1]] + grid[newPos[0] + 1][newPos[1] + 1] + grid[newPos[0]][newPos[1] + 1] \
            + grid[newPos[0] - 1][newPos[1] + 1]
            if data > num:
                grid[newPos[0]][newPos[1]] = data
                check = True
                break
            steps -= 1

        direction += 1

    rowStr = [list(map(str, row)) for row in grid]
    for row in rowStr:
        for ch in row:
            spaces = ' ' * (6 - len(ch))
            print(spaces + ch, end='')
        print()

    return grid

check = False
g = createGrid(265149)
for r, row in enumerate(g):
    if check == True:
        break
    for c, num in enumerate(row):
        if num == 265149:
            p = (r, c)
            check = True
            break

d = len(g) // 2
# print(abs(p[0] - d) + abs(p[1] - d))
maxList = []
for row in createGrid2(265149):
    maxList.append(max(num for num in row))

print(max(maxList))