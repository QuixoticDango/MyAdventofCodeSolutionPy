# target area: x=117..164, y=-140..-89
from math import sqrt
    file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 17 Advent of Code Input.txt"

def consec_int(n: int):
    for i in range(1, n+1):
        yield sum(k for k in range(i+1))

def advance_trajectory(x_rang: tuple[int, int], y_rang: tuple[int, int], x_ivel: int, y_ivel: int,
                       start: tuple[int, int] = (0,0)) -> int | None:
    x_pos = start[0]
    y_pos = start[1]
    steps = 0
    final_y_pos = []
    for i in range(1, x_vel):
        x_pos = (-i^2 + 2 * x_ivel * i + i) // 2
        # if x_pos 
        y_pos = (i+1) * (2 * y_ivel - i) // 2
        if x_pos in range(x_rang[0], x_rang[1] + 1) and y_pos in range(y_rang[0], y_rang[1] + 1):
            final_y_pos.append(y_pos)
        # if x_pos > x_rang[1]

with open(file) as f:
    num = ''
    num_list = []
    num_found = False
    for ch in f.readline():
        if num_found and not ch.isnumeric():
            num_list.append(int(num))
            num = ''
            num_found = False
        if ch == '-' or ch.isnumeric():
            num += ch
            num_found = True
    else:
        num_list.append(int(num))
        
x_rang, y_rang = range(num_list[0], num_list[1]+1), range(num_list[2], num_list[3]+1)

y_init_vel = -(num_list[2] + 1)
max_height = y_init_vel*(y_init_vel + 1) // 2
print(f"Part 1: {max_height}")

max_init_vx = num_list[1]
min_init_vx = 1
for v in range(20):
    if v*(v+1)//2 >= num_list[0]:
        min_init_vx = v
        break
# print(min_init_vx)
# print(max_init_vx)

max_init_vy = -num_list[2] - 1
min_init_vy = num_list[3]-1
for i in range(1000):
    # print(f"{(i+1) * (2*min_init_vy - i) // 2 = }")
    if (i+1) * (2*min_init_vy- i) // 2 < -89:
        break
# print(min_init_vy)

s: set = set()
for vx in range(1, num_list[1]+1):
    for vy in range(num_list[2] - 1, -num_list[2]+1):
        v_x = vx
        v_y = vy
        x_pos = 0
        y_pos = 0
        while x_pos <= num_list[1] and y_pos >= num_list[2]:
            x_pos += v_x
            y_pos += v_y
            if v_x > 0:
                v_x -= 1
            elif v_x < 0:
                v_x += 1
            
            v_y -= 1
            
            if x_pos in x_rang and y_pos in y_rang:
                s.add((vx, vy))
                break

print(f"Part 2: {len(s)}")

# init_x_vels = []
# for n in range(2, num_list[1]+1):
#     init_x_vels = list(enumerate(consec_int(n), 1))
#     if init_x_vels[-1][1] >= num_list[1]:
#         break

# init_x_vels = list(filter(lambda x: x[1] in range(num_list[0], num_list[1]+1), init_x_vels))
# print(init_x_vels)
# ylst =[]
# for y_ivel in range(-1000, 1001):
#     for i in range(init_x_vels[0][0], init_x_vels[-1][0]+1):
#         y = (i+1) * (2 * y_ivel - i) // 2
#         if y in range(num_list[2], num_list[3]+1):
#             ylst.append((i, y_ivel, y))
# y_max_v = max(v for _,v,_ in ylst)
# max_y = y_max_v*(y_max_v+1)//2
# # print(max_y)

# # print(x_rang)
# # print(y_rang)
# x_acc = -1
# x_min_disp = num_list[0]
# x_max_disp = num_list[1]
# y_min_disp = num_list[2]
# y_max_disp = num_list[3]
# x_fvel = 0

"""In the x-dir, we're finding the sum of consecutive, decreasing integers from x_ivel to 
0(at the lowest). 
n(n+1)//2 - [(n-1)(n)//2] : 1st round
n(n+1)//2 - [(n-2)(n-1)//2] : 2nd round
n(n+1)//2 - [(n-i)(n - i + 1)//2] : ith round

n^2/2 + n/2 - (n^2/2 - n*i/2 + n/2 - n*i/2 + i^2/2 - i/2) = D
n*i - i^2/2 + i/2 = D
n*i - i^2/2 + i/2 = D
(-i^2 + 2*n*i + i)//2 = Dx <- formula for x
(i+1) * (2*init_v - i) // 2 = Dy <- formula for y
***x der***
i^2 - 2*n*i - i + 2*Dx = 0
i^2 - (2*n + 1) * i + 2*Dx = 0
((2*n + 1) +/- sqrt((2*n + 1)^2 - 8*Dx)) / 2 = i
***y der***
2*init_v*i - i^2 + 2*init_v - i - 2*Dy = 0
i^2 - 2*init_v*i+i - 2*init_v + 2*Dy = 0
i^2 - (2*init_v - 1) * i - 2*init_v + 2*Dy = 0
((2*init_v - 1) +/- sqrt((2*init_v - 1)^2 + 8*(init_v - Dy)))/2 = i

"""
# print(f"{((2*15 + 1) + sqrt((2*15+1)**2 - 8*120)) / 2 = }")
# print(f"{((2*3 - 1) - sqrt((2*3 - 1)^2 + 8*(3 - -99)))/2 = }")
# for x_vel in range(num_list[1]+1):
# x_vel = 6
# for i in range(x_vel+1):
#     s = (-i**2 + 2 * x_vel * i + i)//2
#     print(f"Round {i} | Round sum = {s} | Full sum = {x_vel*(x_vel+1)//2} | \
#             Minus part = {(x_vel-i)*(x_vel-i+1)//2}")
#     if s > num_list[0] or s in range(num_list[0], num_list[1]+1):
            # break

# for i in range(5, -9, -1):
#     if i >= 0:
#         print(" " + str(i), end='   ')
#     else:
#         print(i, end='   ')
# print()
# for i in range(-8, 6):
#     if i >= 0:
#         print(" " + str(i), end='   ')
#     else:
#         print(i, end='   ')
# print()
# print(f"{sum(i for i in range(-8, 6))}")

# """sum across negative and positive consecutive ints is 
# (abs(final_v - init_v) + 1) * (final_v + init_v) // 2 <<< for y_vel
# final_v = init_v - i
# (abs(-i) + 1) * (init_v - i + init_v) // 2
# (i+1) * (2*init_v - i) // 2 = Dy
# """