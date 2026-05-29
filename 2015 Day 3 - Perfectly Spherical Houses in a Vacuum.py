def houseCount(inst):
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    initPos = (0,0)
    visited = {initPos}
    for ch in inst:
        if ch == '^':
            d = 0
        if ch == '>':
            d = 1
        if ch == 'v':
            d = 2
        if ch == '<':
            d = 3
        newPos = (directions[d][0] + initPos[0], (directions[d][1] + initPos[1]))
        visited.add(newPos)
        initPos = newPos
    return len(visited)

def houseCount2(inst):
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    initPos = (0,0)
    initPosR = (0,0)
    visited = {initPos}
    visitedR = {initPosR}
    for i, ch in enumerate(inst):
        if ch == '^':
            d = 0
        if ch == '>':
            d = 1
        if ch == 'v':
            d = 2
        if ch == '<':
            d = 3
        if i % 2 == 0:    
            newPos = (directions[d][0] + initPos[0], (directions[d][1] + initPos[1]))
            visited.add(newPos)
            initPos = newPos
        else:
            newPosR = (directions[d][0] + initPosR[0], (directions[d][1] + initPosR[1]))
            visitedR.add(newPosR)
            initPosR = newPosR
        
        atLeastOne = visited | visitedR
    return len(atLeastOne)

filePath = "C:\\Users\\lyndo\Documents\\Coding and Programming Folder\\2015 Day 3 Advent of Code Input.txt"
with open(filePath, 'r') as f:
    instructions = f.readline()

print(houseCount2(instructions))