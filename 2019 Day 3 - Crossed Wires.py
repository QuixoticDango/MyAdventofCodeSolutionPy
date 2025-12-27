
def draw_path(instructions):
    current_pos = (0,0)
    positions_reached = set()
    dir = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
    for inst in instructions:
        direction = inst[:1]
        total_steps = int(inst[1:])
        for i in range(1, total_steps + 1):
            current_pos = (current_pos[0] + dir[direction][0], current_pos[1] + dir[direction][1])
            positions_reached.add(current_pos)
    return positions_reached

def count_steps(instructions, intersection):
    current_pos = (0,0)
    dir = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
    step_count = 0
    for inst in instructions:
        direction = inst[:1]
        total_steps = int(inst[1:])
        for i in range(1, total_steps + 1):
            step_count += 1
            current_pos = (current_pos[0] + dir[direction][0], current_pos[1] + dir[direction][1])
            if current_pos == intersection:
                return step_count

def manhattan_distance(p1, p2=(0,0)):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2019 Day 3 Advent of Code Input.txt"

with open(file, 'r') as f:
    first_wire = f.readline().strip().split(',')
    second_wire = f.readline().strip().split(',')

first_path = draw_path(first_wire)
second_path = draw_path(second_wire)

intersection_points = first_path.intersection(second_path)
print(min(manhattan_distance(point) for point in intersection_points if point != 0))
print(min(count_steps(first_wire, intersection) + count_steps(second_wire, intersection) for intersection in intersection_points))

