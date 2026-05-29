filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2016 Day 2 Advent of Code Input.txt"
filePath2 = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2016 Day 2 Advent of Code Input Keypad.txt"

with open(filePath) as f:
    instructions = [line for line in f.readlines()]

def findCode(inst):
    keypad = [[str(i + 1 + 3*j) for i in range(3)] for j in range(3)]
    vPos = 1
    hPos = 1
    code = ''
    for line in inst:
        for ch in line:
            if ch == 'U':
                if vPos - 1 >= 0:
                    vPos -= 1
            if ch == 'L':
                if hPos - 1 >= 0:
                    hPos -= 1
            if ch == 'D':
                if vPos + 1 <= 2:
                    vPos += 1
            if ch == 'R':
                if hPos + 1 <= 2:
                    hPos += 1
        code += keypad[vPos][hPos]
    return code

def findCode2(inst):
    with open(filePath2) as f:
        keydiamond = [line.strip().split() for line in f.readlines()]

        for i, line in enumerate(keydiamond):
            if len(line) < 5:
                numBlanks = (5 - len(line)) // 2
                c = 0
                while c < numBlanks:
                    keydiamond[i].append('')
                    keydiamond[i].insert(0, '')
                    c += 1
    vPos = 2
    hPos = 0
    code = ''
    for line in inst:
        for ch in line:
            if ch == 'U':
                if vPos - 1 >= 0 and keydiamond[vPos-1][hPos] != '':
                    vPos -= 1
            if ch == 'L'and keydiamond[vPos][hPos-1] != '':
                if hPos - 1 >= 0:
                    hPos -= 1
            if ch == 'D':
                if vPos + 1 <= 4:
                    if keydiamond[vPos+1][hPos] != '':
                        vPos += 1
            if ch == 'R':
                if hPos + 1 <= 4:
                    if keydiamond[vPos][hPos+1] != '':
                        hPos += 1
        code += keydiamond[vPos][hPos]
    return code

print(findCode2(instructions))