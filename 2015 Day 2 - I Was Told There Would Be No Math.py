def surfaceAreas(lst):
    sum = 0
    for l,w,h in lst:
        area = 2 * l * w + 2 * l * h + 2 * w * h + min(l*w, w*h, l*h)
        sum += area
    return sum

def length(lst):
    l = 0
    sum = 0
    for l,w,h in lst:
        l = 2 * min(l,w,h) + 2 * min(l*w,l*h,w*h) // min(l,w,h) + l*w*h
        sum += l
    return sum


filePath = "C:\\Users\\lyndo\Documents\\Coding and Programming Folder\\2015 Day 2 Advent of Code Input.txt"
with open(filePath, 'r') as f:
    presents = [tuple(map(int, line.strip().split('x'))) for line in f.readlines()]

print(length(presents))

