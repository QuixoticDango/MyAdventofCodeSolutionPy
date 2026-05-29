def transpose(array):
    T_array = [[0 for col in range(len(array))] for row in range(len(array[0]))]
    for i, row in enumerate(array):
        for j, col in enumerate(row):
            T_array[j][i] = array[i][j]
    return T_array

def decryptMessage(rawText):
    message = ''
    for line in rawText:
        chLst = []
        chDict = dict()
        chIndex = 0
        for ch in line:
            if ch not in chDict.keys():
                chLst.append([ch, 1])
                chDict[ch] = chIndex
                chIndex += 1
            else:
                chLst[chDict[ch]][1] += 1
        maxCount = max(c for ch, c in chLst)
        message += [ch for ch, c in chLst if c == maxCount][0]
    print(message)

def decryptMessage2(rawText):
    message = ''
    for line in rawText:
        chLst = []
        chDict = dict()
        chIndex = 0
        for ch in line:
            if ch not in chDict.keys():
                chLst.append([ch, 1])
                chDict[ch] = chIndex
                chIndex += 1
            else:
                chLst[chDict[ch]][1] += 1
        minCount = min(c for ch, c in chLst)
        message += [ch for ch, c in chLst if c == minCount][0]
    print(message)

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2016 Day 6 Advent of Code Input.txt"

with open(filePath) as f:
    rawData = [line.strip() for line in f.readlines()]
    rawMessage = transpose(rawData)

decryptMessage2(rawMessage)
