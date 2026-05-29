def inBounds(point, field):
    col_max = len(field) - 1
    row_max = len(field[0]) - 1

    if 0 <= point[0] <= col_max and 0 <= point[1] <= row_max:
        return True
    return False

def scoreTrail(field):
    stepDir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    trailheadPos = [(r_i, c_i) for r_i, row in enumerate(field)
                    for c_i, ch in enumerate(row) if ch == '0']
    print(f"{trailheadPos=}")

    score = 0
    for trailhead in trailheadPos:
        point = trailhead
        dir = 0
        try:
            if all(int(field[point[0] + stepDir[i % 4][0]][point[1] + stepDir[i % 4][1]]) - 
                       int(field[point[0]][point[1]]) != 1 for i in range(4)):
                print(f"{i=}")
                continue
        except Exception as e:
            print(e)
            print(f"{i=}")
            pass
        try:
            newPoint = (point[0] + stepDir[dir % 4][0], point[1] + stepDir[dir % 4][1])
            delta = int(field[newPoint[0]][newPoint[1]]) - int(field[point[0]][point[1]])
            print(f"{delta=}")
            if all(int(field[point[0] + stepDir[dir % 4][0]][point[1] + stepDir[dir % 4][1]]) - 
                    int(field[point[0]][point[1]]) != 1 for dir in range(4)):
                print("Reached 1st 'if'.")
                break
            if field[newPoint[0]][newPoint[1]] == '9':
                score += 1
                print("Reached 2nd 'if'.")
                break
            if delta != 1:
                print("Reached 3rd 'if'.")
                dir += 1
                continue
            else:
                print("Reached 'else'.")
                point = newPoint
                print(f"{point=}")
            print(f"{point=}")
        except Exception as e:
            print("Reached 'except'.")
            print(e)
            dir += 1
    return score

file_path = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2024 Day 10 Advent of Code Input Test.txt"
with open(file_path, 'r') as f:
    trail = [row.strip() for row in f.readlines()]

for row in trail:
    print(row)
print()

print(scoreTrail(trail))