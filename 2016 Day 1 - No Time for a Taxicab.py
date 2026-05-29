filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2016 Day 1 Advent of Code Input.txt"
with open(filePath) as f:
    instructions = f.readline().strip().split(', ')
    instructions = [(inst[:1], int(inst[1:])) for inst in instructions]

direction = [(-1,0), (0,1), (1,0), (0,-1)]

def countBlocks(instructions):
    vPos = 0
    hPos = 0
    d = 0
    for turn, steps in instructions:
        if turn == 'R':
            d += 1
        if turn == 'L':
            d -= 1
        if d < 0:
            d += len(direction)
        if d % 2 == 0:
            vPos += direction[d % 4][0] * steps
        if d % 2 == 1:
            hPos += direction[d % 4][1] * steps
    return abs(vPos) + abs(hPos)

def countBlocks2(instructions):
    vPos = 0
    hPos = 0
    d = 0
    visitedPositions = set()
    for turn, steps in instructions:
        if turn == 'R':
            d += 1
        if turn == 'L':
            d -= 1
        if d < 0:
            d += len(direction)
        i = 0
        while i < steps:
            if d % 2 == 0:
                vPos += direction[d % 4][0]
            if d % 2 == 1:
                hPos += direction[d % 4][1]
            if (vPos, hPos) in visitedPositions:
                answer = (vPos, hPos)
                print(answer)
                return abs(vPos) + abs(hPos)
            else:
                visitedPositions.add((vPos, hPos))
            i += 1
    return abs(vPos) + abs(hPos)

print(countBlocks2(instructions))
# print(f"{visitedPositions=}")
# dist = abs(vPos) + abs(hPos)

# print(f"{answer=}")
# print(f"{vPos=}")
# print(f"{hPos=}")
# print(f"{dist=}")