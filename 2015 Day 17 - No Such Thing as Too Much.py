from itertools import combinations

def fillContainers(numList):
    count = 0
    for i in range(4,10):
        for j in combinations(numList, i):
            s = sum(j)    
            if s == 150 and i <= 4:
                count +=1
    return count

# from numpy import vectorize        

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 17 Advent of Code Input.txt"
with open(filePath) as f:
    containers = list(map(int, [line.strip() for line in f.readlines()]))
    containers.sort()

print(fillContainers(containers))
print(containers)
#     x = vectorize(int)(list(f))
# print(1 << len(x))
# c = 0
# for i in range(1 << len(x)):
#     t = i
#     s = 0
#     for j in x:
#         if t % 2 == 1:
#             s += j
#         t //= 2
#     if s == 150:
#         c += 1
# print(c)