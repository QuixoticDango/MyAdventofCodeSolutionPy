def isNice(string):
    vowels = 'aeiou'
    badSeq = ('ab', 'cd', 'pq', 'xy')
    if sum(1 for ch in string if ch in vowels) < 3:
        return False
    if not any(string[i] == string[i+1] for i in range(len(string) - 1)):
        return False
    if any((string[i] + string[i+1]) in badSeq for i in range(len(string) - 1)):
        return False
    return True

def isNice2(string):
    if not any(string[i] + string[i+1] == string[j] + string[j+1] for i in range(0, len(string) - 3)
           for j in range(i+2, len(string) - 1)):
        return False
    if not any(string[i] == string[i+2] for i in range(len(string) - 2)):
        return False
    return True

filePath = "C:\\Users\\lyndo\Documents\\Coding and Programming Folder\\2015 Day 5 Advent of Code Input.txt"
with open(filePath, 'r') as f:
    strings = [line.strip().lower() for line in f.readlines()]

count = 0
for string in strings:
    if isNice2(string):
        count += 1

print(count)