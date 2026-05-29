import re

def makeScreen(width, height):
    screen = [['.' for j in range(width)] for i in range(height)]
    return screen

def updateScreen(com=[['rect', '3x5'], ['rotate column', 'x=2 by 5'],['rotate row', 'y=3 by 4']]):
    screen = makeScreen(50, 6)

    for c, i in com:
        if c == 'rect':
            w, h = list(map(int,i.split('x')))
            for r, row in enumerate(screen):
                for c, ch in enumerate(row):
                    if r < h and c < w:
                        row = ['#' for i in range(w)] + [row[j] for j in range(w, len(row))]
                        screen[r] = row
        for row in screen:
            print(''.join(row))
        print()

        if c == 'rotate row':
            rowIndex, stepString = i.split(' by ')
            rowIndex = int(rowIndex[2:])
            steps = int(stepString)

            i = 0
            row = list(enumerate(screen[rowIndex]))
            newRow = ['' for j in range(50)]

            for c, ch in row:
                newCol = (c + steps) % 50
                newRow[newCol] += ch
            screen[rowIndex] = newRow
        for row in screen:
            print(''.join(row))
        print()

        if c == 'rotate column':
            colIndex, stepString = i.split(' by ')
            colIndex = int(colIndex[2:])
            steps = int(stepString)

            i = 0
            col = list(enumerate(screen[i][colIndex] for i in range(6)))
            newCol = ['' for j in range(6)]

            for r, ch in col:
                newRow = (r + steps) % 6
                newCol[newRow] = [ch]

            for r, row in enumerate(screen):
                screen[r] = row[:colIndex] + newCol[r] + row[colIndex+1:]

        for row in screen:
            print(''.join(row))
        print()
    screen = [''.join(row) for row in screen]
    for row in screen:
        print(''.join(row))
    print()
    return screen
            

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2016 Day 8 Advent of Code Input.txt"
with open(filePath) as f:
    input = [line.strip() for line in f.readlines()]
    commands = [[i[:re.search(r'rect|rotate row|rotate column', i).end()], re.split(r'rect|rotate row|rotate column', i)[1].strip()] for i in input]
# print(commands)
c = sum(1 for row in updateScreen(commands) for ch in row if ch == '#')
print(f"{c=}")