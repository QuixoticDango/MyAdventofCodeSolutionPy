filePath = "C:\\Users\\lyndo\Documents\\Coding and Programming Folder\\2015 Day 1 Advent of Code Input.txt"
with open(filePath, "r") as f:
    rawText = f.readlines()[0].strip()
    floor = 0
    for i, ch in enumerate(rawText, 1):
        if ch == '(':
            floor += 1
        if ch == ')':
            floor -= 1
        if floor == -1:
            index = i
            break
    print(index)