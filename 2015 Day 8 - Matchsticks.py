import re

def part1(strings):
    sumC = 0
    sum = 0 
    for string in strings:
        chrCount = 0
        escCount = 0
        escQuoteCount = 0
        escHexCount = 0
        escPartnerList = []
        s = string[1:len(string) - 1]
        for i, ch in enumerate(s):
            try:    
                if ch + s[i+1] == '\\"':
                    escQuoteCount += 1
                    escPartnerList.append(i+1)
            except IndexError:
                pass
            try:
                if any(ch + s[i+1] + s[i+2] + s[i+3] in re.findall(r'\\x[a-f0-9][a-f0-9]', s) for i in range(len(s)))\
                and escHexCount < len(re.findall(r'\\x[a-z0-9][a-z0-9]', s)):
                    if ch + s[i+1] + s[i+2] + s[i+3] in re.findall(r'\\x[a-f0-9][a-f0-9]', s): 
                        escPartnerList.append(i+1)
                        escPartnerList.append(i+2)
                        escPartnerList.append(i+3)
                        escHexCount += 1
            except IndexError:
                pass
            if ch == '\\' and (i+1) not in escPartnerList:
                escCount += 1
            try:
                if ch != '\\' and i not in escPartnerList:
                    chrCount += 1
            except IndexError:
                pass
        sum += len(string)
        sumC += chrCount + escHexCount + escCount // 2 + escQuoteCount
    return sum - sumC

def part2(strings):
    sum = 0
    newStrCount = 0
    for string in strings:
        sum += len(string)
        s = string[1:len(string) - 1]
        for i,ch in enumerate(s):
            if ch == '\\' or ch == '"':
                newStrCount += 2
            else:
                newStrCount += 1
        newStrCount += 6
    print(f"{newStrCount=}")
    print(f"{sum=}")
    return newStrCount - sum

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 8 Advent of Code Input.txt"
with open(filePath, 'r') as f:
    rawStrings = [line.strip() for line in f.readlines()]

print(f"{part2(rawStrings)=}")
