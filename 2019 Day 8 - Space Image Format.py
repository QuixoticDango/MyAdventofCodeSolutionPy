import numpy as np
from matplotlib import pyplot as plt

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2019 Day 8 Advent of Code Input.txt"

with open(file, 'rt') as f:
    image = [ch for ch in f.readline().strip()]

width = 25
height = 6

num_of_layers = divmod(len(image), 150)[0] + 1 if divmod(len(image), 150)[1] > 0 else divmod(len(image), 150)[0]
layers = [[['' for col in range(25)] for row in range(6)] for layer in range(num_of_layers)]

for i, pixel in enumerate(image):
    layers[i // (width * height)][(i // width) % height][i % width] = pixel

minimum_zeros = 150
for layer in layers:
    zero_count = 0
    for row in layer:
        for ch in row:
            if ch == '0':
                zero_count += 1
    if zero_count < minimum_zeros:
        minimum_zeros = zero_count

fewest_zeros_layer_index = [i for i, layer in enumerate(layers) if sum(1 for row in layer for ch in row if ch == '0') == minimum_zeros][0]

one_two_product = sum(1 for row in layers[fewest_zeros_layer_index] for ch in row if ch == '1') *\
      sum(1 for row in layers[fewest_zeros_layer_index] for ch in row if ch == '2')

print(one_two_product)

# Part 2 answer is EJRGP

pixel_pointer = 0
found_pixel = False
final_message = []
for r in range(height):
    for c in range(width):
        for l in layers:
            if l[r][c] in '01':
                final_message.append((r, c, l[r][c]))
                break
shape = (6, 25)
arr = np.array([int(ch) for i, j, ch in final_message]).reshape(shape)
plt.imshow(arr)
plt.show()