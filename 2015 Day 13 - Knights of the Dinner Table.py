import re
import sys
from itertools import permutations

def scoreList(l, d):
    maxScore = -sys.maxsize

    for t in permutations(l):
        sum = 0
        for i in range(len(t)):
            sum += d[(t[i],t[(i+1) % len(t)])] + d[(t[(i+1) % len(t)],t[(i)])]
        if sum > maxScore:
            maxScore = sum
    return maxScore

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 13 Advent of Code Input.txt"
with open(filePath)as f:
    strings = f.readlines()

p1 = re.compile(r'[a-zA-Z]+\b')
p2 = re.compile(r'[a-zA-Z]+\.')
p3 = re.compile(r'gain|lose \d+')
guests = list({line[:re.search(p1, line).end()].strip()
            for line in strings})
points = {(line[:re.search(p1, line).end()].strip(),
           line[re.search(p2, line).start():line.index('.')]):
           (int(line[re.search(p3, line).start():].split()[1])
            if line[re.search(p3, line).start():].split()[0] == 'gain'
            else -int(line[re.search(p3, line).start():].split()[1]))
            for line in strings}

for person in guests:
    points[(person, 'Jazzman')] = 0
    points[('Jazzman', person)] = 0
guests.append('Jazzman')

print(scoreList(guests, points))
