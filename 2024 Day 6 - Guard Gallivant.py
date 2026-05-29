def markPath(array):
    for i in range(len(array)):
        if array[i].find('^') != -1:
            init_pos = [i, array[i].find('^')]
    
    heading = ('up', 'right', 'down', 'left')
    current_pos = [init_pos[0], init_pos[1]]
    new_pos = [0, 0]
    steps = 0
    direction = 0
    while True:
        array[current_pos[0]] = array[current_pos[0]][0:current_pos[1]] + 'X' + array[current_pos[0]][current_pos[1] + 1:]
        
        if heading[direction] == 'up':
            new_pos[0], new_pos[1] = current_pos[0] - 1, current_pos[1]
        if heading[direction] == 'down':
            new_pos[0], new_pos[1] = current_pos[0] + 1, current_pos[1]
        if heading[direction] == 'right':
            new_pos[0], new_pos[1] = current_pos[0], current_pos[1] + 1
        if heading[direction] == 'left':
            new_pos[0], new_pos[1] = current_pos[0], current_pos[1] - 1
        try:
            if array[new_pos[0]][new_pos[1]] == '#':
                direction = (direction + 1) % 4
                continue
        except IndexError:
            break
        current_pos[0], current_pos[1] = new_pos[0], new_pos[1]
    for row in array:
        for i in range(len(row)):
            if row[i] == 'X':
                steps += 1
    return steps

def displacement(init_pos, final_pos):
    d = ((init_pos[0] - final_pos[0])**2 + (init_pos[1] - final_pos[1])**2)**0.5
    return d

# Rotates grid 90 degrees counterclockwise
def rotateGrid(array):
    rotated_array = [['' for j in range(len(array))] for i in range(len(array[0]))]
    print("Original map.")
    for row in array:
        print(row)
    print()

    for row in range(len(array)):
        for col in range(len(array[0])):
            rotated_array[col][row] = array[row][len(array[0]) - 1 - col]
    
    print("Rotated map.")
    rotated_map = []
    for row in rotated_array:
        rotated_map.append(''.join(row))
    return rotated_map


def findplaceLoops(array):
    for i in range(len(array)):
        if array[i].find('^') != -1:
            init_pos = (i, array[i].find('^'))
    
    heading = ('up', 'right', 'down', 'left')
    current_pos = [init_pos[0], init_pos[1]]
    new_pos = [0, 0]
    turn_loc = []
    direction = 0
    while True:
        if heading[direction] == 'up':
            new_pos[0], new_pos[1] = current_pos[0] - 1, current_pos[1]
        if heading[direction] == 'down':
            new_pos[0], new_pos[1] = current_pos[0] + 1, current_pos[1]
        if heading[direction] == 'right':
            new_pos[0], new_pos[1] = current_pos[0], current_pos[1] + 1
        if heading[direction] == 'left':
            new_pos[0], new_pos[1] = current_pos[0], current_pos[1] - 1
        try:
            if array[new_pos[0]][new_pos[1]] == '#':
                if heading[direction] == 'up':
                    turn_loc.append((new_pos[0] + 1, new_pos[1]))
                if heading[direction] == 'down':
                    turn_loc.append((new_pos[0] - 1, new_pos[1]))
                if heading[direction] == 'right':
                    turn_loc.append((new_pos[0], new_pos[1] - 1))
                if heading[direction] == 'left':
                    turn_loc.append((new_pos[0], new_pos[1] + 1))
                direction = (direction + 1) % 4
                continue
        except IndexError:
            break
        current_pos[0], current_pos[1] = new_pos[0], new_pos[1]
    
    placements = 0
    heading_loc = tuple(enumerate(turn_loc))
    for i in range(len(heading_loc) - 3):
        approach_dir = heading_loc[i][0] % 4
        if i < len(heading_loc) - 3:
            if heading[approach_dir] == 'up':
                if heading_loc[i+3][1][1] < heading_loc[i][1][1] < heading_loc[i+2][1][1]:
                    placements += 1
            if heading[approach_dir] == 'right':
                if heading_loc[i+3][1][0] < heading_loc[i][1][0] < heading_loc[i+2][1][0]:
                    placements += 1
            if heading[approach_dir] == 'down':
                if heading_loc[i+2][1][1] < heading_loc[i][1][1] < heading_loc[i+3][1][1]:
                    placements += 1
            if heading[approach_dir] == 'left':
                if heading_loc[i+2][1][0] < heading_loc[i][1][0] < heading_loc[i+3][1][0]:
                    placements += 1
        else:
            pass
    print(heading_loc)
    # for i in range(len(heading_loc) - 3):
    #     approach_dir = heading_loc[i][0] % 4
    #     if i < len(heading_loc) - 3:
    #         if heading[approach_dir] == 'up':
    #             if heading_loc[i+3][1][1] < heading_loc[i][1][1] < heading_loc[i+2][1][1]:
    #                 test = [[heading_loc[i+3][1][1] < heading_loc[j][1][1] < heading_loc[i+2][1][1] for j in range(len(heading_loc))] for i in range(len(heading_loc) - 3) if heading_loc[j][0] % 4 == 0]
    #                 print(test)
    #         if heading[approach_dir] == 'right':
    #             if heading_loc[i+3][1][0] < heading_loc[i][1][0] < heading_loc[i+2][1][0]:
    #                 placements += 1
    #         if heading[approach_dir] == 'down':
    #             if heading_loc[i+2][1][1] < heading_loc[i][1][1] < heading_loc[i+3][1][1]:
    #                 placements += 1
    #         if heading[approach_dir] == 'left':
    #             if heading_loc[i+2][1][0] < heading_loc[i][1][0] < heading_loc[i+3][1][0]:
    #                 placements += 1
    return placements

    """
    - Facts of life:
        - The first heading is always up.
        - Turns are always 90 degrees clockwise (to the right)
        - The dimension that changes and how it changes alternates.
            - First dimension decreases from initial position (going up) (turn right)
            - Second dimension increases (going right) (turn right)
            - First dimesion increases (going down) (turn right)
            - Second dimension decreases (going left)
    - Points will be checked in sets of three. If an obstacle can be placed after the third turn such
      that it leads back to the first point in the set, then we have an answer.
    - Properties of this point:
        - This point must be in the bounds of the grid. If it isn't, no such placement is possible.
        - The point must force the turn location to be on the same row or column as the first point.
            - ***If this point lies beyond a hash that's already present, this point cannot be placed.
                 Otherwise, it certainly exists provided that it's in the grid***
            - This will depend on:
                - The heading after the third turn which will dimension and direction of change I must examine
                - The current turn location
                - The following turn location
        - The obstacle must be on a point that is 1 greater or 1 less than the turn location in only
          one dimension
        
    """

    # for i in range(len(turn_loc) - 2):
    #     if heading[direction] == 'up' and turn_loc[i+1][0] == turn_loc[i][0] + 1 \
    #     and turn_loc[i+2][]
        

file_path = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2024 Day 6 Advent of Code Input Test.txt"
with open(file_path, 'r') as f:
    guard_map = [row.strip() for row in f.readlines()]

# print(markPath(guard_map))
print(findplaceLoops(guard_map))
# for row in guard_map:    
#     print(row)