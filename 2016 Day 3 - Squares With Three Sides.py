def isTriangle(sides):
    if any(sides[i] + sides[j] <= sides[k] for i in range(3) for j in range(3) for k in range(3) 
           if i != j and i != k and j != k):
        return False
    return True

def transpose(array):
    T_array = [[0 for col in range(len(array))] for row in range(len(array[0]))]
    for i, row in enumerate(array):
        for j, col in enumerate(row):
            T_array[j][i] = array[i][j]
    return T_array

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2016 Day 3 Advent of Code Input.txt"

# with open(filePath) as f:
#     numList = [line.strip().split() for line in f.readlines()]
#     shapes = [tuple(map(int,[a,b,c])) for a,b,c in numList]

# c = 0
# for shape in shapes:
#     if isTriangle(shape):
#         c += 1

# print(f"{c=}")

# Part 2

with open(filePath) as f:
    numList = [line.strip().split() for line in f.readlines()]
    shapes = [list(map(int,[a,b,c])) for a,b,c in numList]

T_shapes = []
for row in transpose(shapes):
    for i in range(len(row)):
        if i % 3 == 0 and i <= len(row) - 3:
            T_shapes.append((row[i], row[i+1], row[i+2]))

c = 0
for sides in T_shapes:
    if isTriangle(sides):
        c += 1

print(f"{c=}")

# print(transpose(shapes))