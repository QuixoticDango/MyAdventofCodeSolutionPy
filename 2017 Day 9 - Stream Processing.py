import re

filename = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2017 Day 9 Advent of Code Input.txt"

with open(filename) as f:
    stream = f.read().strip()
s = stream
idx = 0

score_total = 0
uncanc = 0

stack = []
cscore = 0
garbage = False

while True:
    if idx >= len(s):
        break
    if s[idx] == "!":
        idx += 1
    elif garbage:
        if s[idx] == ">":
            garbage = False
        else:
            uncanc += 1
    elif s[idx] == "{":
        cscore += 1
        stack.append(cscore)
    elif s[idx] == "<":
        garbage = True
    elif s[idx] == "}":
        cscore -= 1
        score_total += stack.pop()
    idx += 1

part = 2
if part == 1:
    result = score_total
    print (result)
else:
    result = uncanc
    print(result)