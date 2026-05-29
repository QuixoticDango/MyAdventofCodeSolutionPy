def codeSort(chList):
    changes = 1
    while changes:
        changes = 0
        for i, [ch, count] in enumerate(chList):
            if i < len(chList)-1 and count < chList[i+1][1]:
                chList = chList[:i] + chList[i+1:i+2] + chList[i:i+1] + chList[i+2:]
                changes += 1

            if i < len(chList)-1 and count == chList[i+1][1]:
                if ch > chList[i+1][0]:
                    chList = chList[:i] + chList[i+1:i+2] + chList[i:i+1] + chList[i+2:]
                    changes += 1
    return chList

def roomIsReal(fullCode):
    name = fullCode[:-7]
    checkSum = fullCode[-6:len(fullCode)-1]
    chSet = []
    chDict = dict()
    chIndex = 0

    for ch in name:
        if ch.isalpha():
            if ch not in chDict.keys():
                chDict[ch] = chIndex
                chSet.append([ch, 1])
                chIndex += 1
            else:
                chSet[chDict[ch]][1] += 1
    
    checkStr = ''
    for i in range(5):
        checkStr += codeSort(chSet)[i][0]
    
    if checkStr == checkSum:
        return True
    return False

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2016 Day 4 Advent of Code Input.txt"

with open(filePath) as f:
    roomNames = [line.strip() for line in f.readlines()]

c = sum(int(room[-10:-7]) for room in roomNames if roomIsReal(room))
# print(f"{c=}")

# Part 2

def decryptName(realRoom):
    sectorID = int(realRoom[-10:-7])
    name = realRoom[:-11]
    
    decryptedName = ''
    for ch in name:
        if ch != '-':
            decryptedName += chr((ord(ch) - ord('a') + sectorID) % 26 + ord('a'))
        else:
            decryptedName += ' '
    return decryptedName

for room in roomNames:
    if roomIsReal(room):
        if decryptName(room).find('north') != -1:
            print(decryptName(room), room[-10:-7])
