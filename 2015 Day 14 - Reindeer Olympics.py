import re

def distance(d):
    maxDist = 0
    for key in d.keys():
        intDist= d[key][0] * d[key][1]
        intervals = time // (d[key][1] + d[key][2])
        intFloat = time / (d[key][1] + d[key][2])
        secondsLeft = time - intervals * (d[key][1] + d[key][2])
        if secondsLeft > 0 and secondsLeft < d[key][1]:
            dist = intervals * intDist + d[key][0] * secondsLeft
        if secondsLeft >= d[key][1]:
            dist = intervals * intDist + d[key][0] * d[key][1]
        print()
        print(f"{key=}")
        print(f"{intDist=}")
        print(f"{intervals=}")
        print(f"{intFloat=}")
        print(f"{(intFloat - intervals) * (d[key][1] + d[key][2])=}")
        print(f"{secondsLeft=}")
        print(f"{dist=}")
        d[key].append(dist)
        if dist > maxDist:
            maxDist = dist
    print(d)
    return maxDist

def points(d):
    for key in d.keys():
        d[key].append(0)
        d[key].append(0)

    i = 0
    while i < time:
        for key in d.keys():
            if i % (d[key][1] + d[key][2]) < d[key][1]:
                d[key][3] += d[key][0]

        for key in d.keys():
            if d[key][3] == max(d[k][3] for k in d.keys()):
                d[key][4] += 1
        
        i += 1

    return max(d[n][4] for n in d.keys())
        

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 14 Advent of Code Input.txt"
with open(filePath)as f:
    strings = f.readlines()

time = 2503
p = re.compile(r'\d+ km\\s')
reindeer = [line[:line.index(' ')] for line in strings]
data = [list(map(int, [line.split()[3],line.split()[6], line.split()[13]]))
        for line in strings]
reindeerData = dict(zip(reindeer, data))
print(points(reindeerData))