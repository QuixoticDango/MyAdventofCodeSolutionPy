# # from itertools import combinations

# # def taxicab_distance(p1, p2):
# #     return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# # def find_area(val, grid):
# #     return sum(1 for key in grid.keys() if grid[key] == val)


# # file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2018 Day 6 Advent of Code Input.txt"


# # with open(file, 'rt') as f:
# #     coordinates = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

# # max_dimensions = tuple((max(row for row, col in coordinates), max(col for row, col in coordinates)))
# # min_dimensions = tuple((min(row for row, col in coordinates), min(col for row, col in coordinates)))
# # count = 0
# # carry = 0
# # grid = {}
# # values = []

# # for i in range(min_dimensions[0], max_dimensions[0]+1):
# #     for j in range(min_dimensions[1], max_dimensions[1]+1):
# #         if (i, j) in coordinates:
# #             grid[(i, j)] = chr(ord('A') + count)
# #             values = chr(ord('A') + count)
# #             count += 1
# #             if count == 26:
# #                 count += 6
# #         else:
# #             grid[(i, j)] = '.'
# # # print(len(grid.keys()))
# # # print(sum(1 for key in grid.keys() if grid[key].isalpha()))

# # count = 0
# # for p1 in grid.keys():
# #     print(f"Currently on point {p1}")
# #     nearest_neighbors = []
# #     step = 1
# #     try:
# #         while not nearest_neighbors:
# #             # print(f"Current iteration: {count}")
# #             for i in range(-step, step + 1, 1):
# #                 for j in range(-step, step + 1, 1):
# #                     # print(f"{(p1[0] + i, p1[1] + j)=}")
# #                     if i == 0 and j == 0:
# #                         continue
# #                     if (p1[0] + i, p1[1] + j) in coordinates:
# #                         # print(f"what? {p1=}")
# #                         # print(f"{p1[0]=}, {p1[0]=}")
# #                         # print(f"NEIGHBOR: {p1[0] + i, p1[1] + j}")
# #                         nearest_neighbors.append((p1[0] + i, p1[1] + j))
# #                         # print(f"NEAREST NEIGHBORS: {nearest_neighbors}")
# #             step += 1
# #             count += 1
# #         if len(nearest_neighbors) == 1:
# #             grid[p1] = grid[nearest_neighbors[0]]
# #         if len(nearest_neighbors) > 1:
# #             min_dist = min(taxicab_distance(p1, nearest_neighbors[i]) 
# #                            for i in range(len(nearest_neighbors)))
# #             checklist = [neighbor for neighbor in nearest_neighbors 
# #                          if taxicab_distance(p1, neighbor) == min_dist]
# #             if len(checklist) == 1:
# #                 # print('CHECKLIST IS UNIQUE')
# #                 grid[p1] = grid[checklist[0]]
# #     except KeyError:
# #         # print(f"ERROR! But it's ok: ({i}, {j})")
# #         pass
# #     # if p1 in coordinates:
# #     #     continue
# #     # min_dist = min(taxicab_distance(p1, p2) for p2 in coordinates)
# #     # checklist = [p for p in coordinates if taxicab_distance(p1, p) == min_dist]
# #     # if len(checklist) == 1:
# #     #     print("made it to checklist")
# #     #     grid[p1] = grid[checklist[0]]
# # print("PAST THE GIANT LOOP")
# # max_area = max(find_area(v, grid) for v in values)
# # max_values = [v for v in values if find_area(v, grid) == max_area]
# # print(max_values)
# # print(sum(1 for key in grid.keys() if grid[key] == max_values[0]))

# import numpy as np
# from scipy.spatial import distance

# # read the data using scipy
# file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2018 Day 6 Advent of Code Input.txt"
# points = np.loadtxt(file, delimiter=',')

# # build a grid of the appropriate size - note the -1 and +2 to ensure all points
# # are within the grid
# # print(points.min(axis=0))
# # print(points)
# xmin, ymin = points.min(axis=0) - 1
# xmax, ymax = points.max(axis=0) + 2

# # and use mesgrid to build the target coordinates
# xgrid, ygrid = np.meshgrid(np.arange(xmin, xmax), np.arange(xmin, xmax))
# targets = np.dstack([xgrid, ygrid]).reshape(-1, 2)
# print(targets)

# # happily scipy.spatial.distance has cityblock (or manhatten) distance out
# # of the box
# cityblock = distance.cdist(points, targets, metric='cityblock')
# # the resulting array is an input points x target points array
# # so get the index of the maximum along axis 0 to tie each target coordinate
# # to closest ID
# closest_origin = np.argmin(cityblock, axis=0)
# # we need to filter out points with competing closest IDs though
# min_distances = np.min(cityblock, axis=0)
# competing_locations_filter = (cityblock == min_distances).sum(axis=0) > 1
# # note, integers in numpy don't support NaN, so make the ID higher than
# # the possible point ID
# closest_origin[competing_locations_filter] = len(points) + 1
# # and those points around the edge of the region for "infinite" regions
# closest_origin = closest_origin.reshape(xgrid.shape)
# infinite_ids = np.unique(np.vstack([
#     closest_origin[0],
#     closest_origin[-1],
#     closest_origin[:, 0],
#     closest_origin[:, -1]
# ]))
# closest_origin[np.isin(closest_origin, infinite_ids)] = len(points) + 1

# # and because we know the id of the "null" data is guaranteed to be last
# # in the array (it's highest) we can index it out before getting the max
# # region size
# print(np.max(np.bincount(closest_origin.ravel())[:-1]))

# # finally, make a pretty picture for good measure
# import matplotlib.pyplot as plt
# plt.imshow(np.where(closest_origin > len(points), np.nan, closest_origin))
# plt.colorbar()
# plt.show()

import numpy as np
from scipy.spatial import distance

# read the data using scipy
points = np.loadtxt(r"C:\Users\lyndo\Documents\Coding and Programming Folder\2018 Day 6 Advent of Code Input.txt", delimiter=',')   

# build a grid of the appropriate size - note the -1 and +2 to ensure all points
# are within the grid
xmin, ymin = points.min(axis=0) - 1
xmax, ymax = points.max(axis=0) + 2

# and use mesgrid to build the target coordinates
xgrid, ygrid = np.meshgrid(np.arange(xmin, xmax), np.arange(xmin, xmax))
targets = np.dstack([xgrid, ygrid]).reshape(-1, 2)

# happily scipy.spatial.distance has cityblock (or manhatten) distance out
# of the box
cityblock = distance.cdist(points, targets, metric='cityblock')

# turns out using this method the solution is easier that before - simply
# sum the distances for each possible grid location
origin_distances = cityblock.sum(axis=0)
# set the value of appropriate distances to 1, with the remainder as zero
region = np.where(origin_distances < 10000, 1, 0)
# and the sum is the result.
print(region.sum())

# again, a nice picture for good measure
import matplotlib.pyplot as plt
plt.imshow(region.reshape(xgrid.shape))
plt.colorbar()
plt.show()