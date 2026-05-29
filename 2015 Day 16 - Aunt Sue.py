
# filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 16 Advent of Code Input.txt"
# with open(filePath) as f:
#     rawData = f.readlines()
#     Sues = {line.strip()[:line.find(':')]:set(line.strip()[line.find(':') + 2:].split(', ')) for line in rawData}

# filePath2 = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 16 Advent of Code Input Real Sue.txt"
# with open(filePath2) as g:
#     realSue = {line.strip() for line in g}

# # Part 1
# realSueNum = [key for key in Sues.keys() if Sues[key] < realSue]
# print(realSueNum)

# Part 2

def isRealSue(dList, rD):
    if any(dList[key] != rD[key] for key in dList.keys()
           if key != 'cats' and key != 'trees' and key != 'pomeranians' and key != 'goldfish'):
        return False
    if 'cats' in dList.keys() and dList['cats'] <= rD['cats']:
        return False
    if 'trees' in dList.keys() and dList['trees'] <= rD['trees']:
        return False
    if 'pomeranians' in dList.keys() and dList['pomeranians'] >= rD['pomeranians']:
        return False
    if 'goldfish' in dList.keys() and dList['goldfish'] >= rD['goldfish']:
        return False
    return True

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 16 Advent of Code Input.txt"
with open(filePath) as f:
    rawData = f.readlines()
    Sues = {line.strip()[:line.find(':')]:list(line.strip()[line.find(':') + 2:].split(', ')) for line in rawData}

filePath2 = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 16 Advent of Code Input Real Sue.txt"
with open(filePath2) as g:
    realSue = {line.strip().split(': ')[0]:int(line.strip().split(': ')[1]) for line in g}

for key in Sues.keys():
    valueDicts = {val.split(': ')[0]:int(val.split(': ')[1]) for val in Sues[key]}
    Sues[key] = valueDicts

# print(any(Sues["Sue 40"][key] != realSue[key] for key in Sues['Sue 40'].keys() if key != 'cats' and key != 'trees' and key != 'pomeranians' and key != 'goldfish'))

for key in Sues.keys():
    if isRealSue(Sues[key], realSue):
        print(key + ':', f'{Sues[key]=}')