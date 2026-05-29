import re

def lightState(inst, starts, ends):
    grid = [[False for col in range(1000)] for row in range(1000)]

    for i, (sR, sC) in enumerate(starts):
        if inst[i] == "turn on":
            for row in range(sR, ends[i][0] + 1):
                for col in range(sC, ends[i][1] + 1):
                    grid[row][col] = True
        if inst[i] == "turn off":
            for row in range(sR, ends[i][0] + 1):
                for col in range(sC, ends[i][1] + 1):
                    grid[row][col] = False
        if inst[i] == "toggle":
            for row in range(sR, ends[i][0] + 1):
                for col in range(sC, ends[i][1] + 1):
                    grid[row][col] = not grid[row][col]
    
    count = 0
    for row in grid:
        for col in row:
            if col:
                count += 1
    return count

def lightState2(inst, starts, ends):
    grid = [[0 for col in range(1000)] for row in range(1000)]

    for i, (sR, sC) in enumerate(starts):
        if inst[i] == "turn on":
            for row in range(sR, ends[i][0] + 1):
                for col in range(sC, ends[i][1] + 1):
                    grid[row][col] += 1
        if inst[i] == "turn off":
            for row in range(sR, ends[i][0] + 1):
                for col in range(sC, ends[i][1] + 1):
                    if grid[row][col] > 0:
                        grid[row][col] -= 1
        if inst[i] == "toggle":
            for row in range(sR, ends[i][0] + 1):
                for col in range(sC, ends[i][1] + 1):
                    grid[row][col] += 2
    sum = 0
    for row in grid:
        for col in row:
            sum += col
    return sum

        

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 6 Advent of Code Input.txt"
with open(filePath, 'r') as f:
    instructions = [string[re.search(r"turn on|turn off|toggle", string).start():re.search(r"turn on|turn off|toggle", string).end()] 
                          for string in [line.strip() for line in f.readlines()]]

with open(filePath, 'r') as f:
    startPos = [tuple(map(int, string[re.search(r'\d+\,\d+', string).start():re.search(r'\d+\,\d+', string).end()].split(','))) 
                    for string in [line.strip() for line in f.readlines()]]

with open (filePath, 'r') as f: 
    endPos = [tuple(map(int, string.split(','))) 
              for string in [line.strip().split('through')[1] for line in f.readlines()]]
    
print(lightState2(instructions, startPos, endPos))