import re

def IPisValid(address):
    p1 = re.compile(r"\[([a-z]+)\]")
    subStrings = re.split(p1, address)
    sOut = subStrings[::2]
    sIn = subStrings[1::2]
    
    if any(a == d and b == c and a != b for s in sIn for a,b,c,d in zip(s, s[1:], s[2:], s[3:])):
        return False
    if any(a == d and b == c and a != b for s in sOut for a,b,c,d in zip(s, s[1:], s[2:], s[3:])):
        return True
    else:
        return False
def IPisValid2(address):
    p1 = re.compile(r"\[([a-z]+)\]")
    subStrings = re.split(p1, address)
    sOut = subStrings[::2]
    sIn = subStrings[1::2]
    o = ' '. join(sOut)
    i = ' '.join(sIn)
    insAndOuts = (' '.join(sOut), ' '.join(sIn))
    
    if any(a == c and a != b and any(b+a+b in t for t in sIn) for s in sOut for a, b, c in zip(s, s[1:], s[2:])):
        return True
    return False

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2016 Day 7 Advent of Code Input.txt"
with open(filePath) as f:
    IPaddresses = [line.strip() for line in f.readlines()]

c = sum(1 for IP in IPaddresses if IPisValid2(IP))

print(f"{c=}")