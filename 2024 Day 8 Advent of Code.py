def inBounds(point, field):
    col_max = len(field) - 1
    row_max = len(field[0]) - 1

    if 0 <= point[0] <= col_max and 0 <= point[1] <= row_max:
        return True
    return False

# Function for Part 1
def markAntinodes(field):
    antennaPos = [(ch, (r_index, c_index)) for r_index, row in enumerate(field)
                    for c_index, ch in enumerate(row) if ch.isalnum()]
    antennaTypes = list({ch for row in field for ch in row if ch.isalnum()})
    antennaDict = {antenna:[] for antenna in antennaTypes}
    pointDict = {(r_index, c_index):[ch] for r_index, row in enumerate(field)
                    for c_index, ch in enumerate(row) if ch.isalnum()}

    for antenna in antennaTypes:
        for ch, point in antennaPos:
            if ch == antenna:
                antennaDict[ch].append(point)
    
    for key in antennaTypes:
        for p1 in range(len(antennaDict[key]) - 1):
            for p2 in range(p1 + 1, len(antennaDict[key])):
                row_d = antennaDict[key][p2][0] - antennaDict[key][p1][0]
                col_d = antennaDict[key][p2][1] - antennaDict[key][p1][1]
                hash1 = (antennaDict[key][p1][0] - row_d, antennaDict[key][p1][1] - col_d)
                hash2 = (antennaDict[key][p2][0] + row_d, antennaDict[key][p2][1] + col_d)
                if not (inBounds(hash1, field) or inBounds(hash2, field)):
                    continue
                if inBounds(hash1, field) and field[hash1[0]][hash1[1]] == '.':
                    field[hash1[0]] = field[hash1[0]][:hash1[1]] + '#' + field[hash1[0]][hash1[1] + 1:len(field[hash1[0]])]
                if inBounds(hash1, field) and field[hash1[0]][hash1[1]].isalnum():
                    if "#" not in pointDict[hash1]:
                        pointDict[hash1].append('#')
                if inBounds(hash2, field) and field[hash2[0]][hash2[1]] == '.':
                    field[hash2[0]] = field[hash2[0]][:hash2[1]] + '#' + field[hash2[0]][hash2[1] + 1:len(field[hash2[0]])]
                if inBounds(hash2, field) and field[hash2[0]][hash2[1]].isalnum():
                    if "#" not in pointDict[hash2]:
                        pointDict[hash2].append('#')
    hashCount = 0

    for row in field:
        for ch in row:
            if ch == '#':
                hashCount += 1

    for key in list(pointDict.keys()):
        for i in range(len(pointDict[key])):
            if pointDict[key][i] == "#":
                hashCount += 1

    return hashCount

# Function for Part 2
def markHarmonics(field):
    antennaPos = [(ch, (r_index, c_index)) for r_index, row in enumerate(field)
                    for c_index, ch in enumerate(row) if ch.isalnum()]
    antennaTypes = list({ch for row in field for ch in row if ch.isalnum()})
    antennaDict = {antenna:[] for antenna in antennaTypes}
    pointDict = {(r_index, c_index):[ch] for r_index, row in enumerate(field)
                    for c_index, ch in enumerate(row) if ch.isalnum()}

    for antenna in antennaTypes:
        for ch, point in antennaPos:
            if ch == antenna:
                antennaDict[ch].append(point)
    
    for key in antennaTypes:
        for p1 in range(len(antennaDict[key]) - 1):
            for p2 in range(p1 + 1, len(antennaDict[key])):
                row_d = antennaDict[key][p2][0] - antennaDict[key][p1][0]
                col_d = antennaDict[key][p2][1] - antennaDict[key][p1][1]
                hash1 = (0,0)
                hash2 = (0,0)
                loopCount = 0
                while inBounds(hash1, field) or inBounds(hash2, field):    
                    hash1 = (antennaDict[key][p1][0] - row_d * loopCount, antennaDict[key][p1][1] - col_d * loopCount)
                    hash2 = (antennaDict[key][p2][0] + row_d * loopCount, antennaDict[key][p2][1] + col_d * loopCount)
                    
                    if not (inBounds(hash1, field) or inBounds(hash2, field)):
                        continue
                    if inBounds(hash1, field) and field[hash1[0]][hash1[1]] == '.':
                        field[hash1[0]] = field[hash1[0]][:hash1[1]] + '#' + field[hash1[0]][hash1[1] + 1:len(field[hash1[0]])]
                    if inBounds(hash1, field) and field[hash1[0]][hash1[1]].isalnum():
                        if "#" not in pointDict[hash1]:
                            pointDict[hash1].append('#')
                    if inBounds(hash2, field) and field[hash2[0]][hash2[1]] == '.':
                        field[hash2[0]] = field[hash2[0]][:hash2[1]] + '#' + field[hash2[0]][hash2[1] + 1:len(field[hash2[0]])]
                    if inBounds(hash2, field) and field[hash2[0]][hash2[1]].isalnum():
                        if "#" not in pointDict[hash2]:
                            pointDict[hash2].append('#')
                    loopCount += 1
                    
    
    for row in field:
        print(row)
    print()

    hashCount = 0
    for row in field:
        for ch in row:
            if ch == '#':
                hashCount += 1

    for key in list(pointDict.keys()):
        for i in range(len(pointDict[key])):
            if pointDict[key][i] == "#":
                hashCount += 1

    return hashCount

file_path = "C:\\Users\\ANON\\Documents\\Coding and Programming Folder\\2024 Day 8 Advent of Code Input.txt"
with open(file_path, 'r') as f:
    antennaMap = [row.strip() for row in f.readlines()]

for row in antennaMap:
    print(row)
print()

print(f"Part 1: {markAntinodes(antennaMap)=}")
print(f"Part 2: {markHarmonics(antennaMap)=}")
