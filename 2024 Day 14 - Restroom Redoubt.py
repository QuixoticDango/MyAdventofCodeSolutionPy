import re, time

def safetyFactor(posVelList):
    cols = 101
    rows = 103
    ebhq = [''.join(['.' for j in range(cols)]) for i in range(rows)]
    for line in ebhq:
        print(line)
    print()
    
    finPos = []
    for pos, vel in posVelList:
        fin_col = (vel[0] * 100 + pos[0]) % cols
        fin_row = (vel[1] * 100 + pos[1]) % rows
        finPos.append((fin_col, fin_row))

    for col, row in finPos:
        ebhq[row] = ebhq[row][:col] + "R" + ebhq[row][col + 1:]

    for line in ebhq:
        print(line)
    print()
    
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for col, row in finPos:
        if cols // 2 < col < cols and 0 <= row < rows // 2:
            q1 += 1
        if 0 <= col < cols // 2 and 0 <= row < rows // 2:
            q2 += 1
        if 0 <= col < cols // 2 and rows // 2 < row < rows:
            q3 += 1
        if cols // 2 < col < cols and rows // 2 < row < rows:
            q4 += 1
    factor = q1 * q2 * q3 * q4
    
    return factor

def findEasterEgg(posVelList):
    cols = 101
    rows = 103
    i = 0
    while i <= 7809:
        ebhq = [''.join(['.' for j in range(cols)]) for i in range(rows)]    
        finPos = []
        for pos, vel in posVelList:
            fin_col = (vel[0] * i + pos[0]) % cols
            fin_row = (vel[1] * i + pos[1]) % rows
            finPos.append((fin_col, fin_row))

        for col, row in finPos:
            ebhq[row] = ebhq[row][:col] + "R" + ebhq[row][col + 1:]

        if any(sum(1 for ch in line if ch == "R") >= 20 for line in ebhq):
            for line in ebhq:
                print(line)
            print(f"{i=} seconds have passed.")
            print()
        i += 1
        

file_path = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2024 Day 14 Advent of Code Input.txt"
with open(file_path, "r") as f:
    lines = [line.strip() for line in f.readlines()]
    initPosVel = []
    start = 0
    for line in lines:
        searchPos = re.search(r"p=[+-]?\d+\,[+-]?\d+", line)
        searchVel = re.search(r"v=[+-]?\d+\,[+-]?\d+", line)
        initPos = tuple(map(int, line[2:searchPos.end()].split(',')))
        initVel = tuple(map(int, line[searchVel.start() + 2:searchVel.end()].split(',')))
        initPosVel.append((initPos, initVel))

print(findEasterEgg(initPosVel))