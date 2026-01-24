file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 5 Advent of Code Input.txt"

def find_location(seed):
    found = False
    for key in seed_soil.keys():
        start, end = key
        if start <= seed <= end:
            # print(f"{key=}")
            # print(f"{seed_soil[key]=}")
            soil = seed_soil[key][0] + (seed - start)
            found = True
            break
    if not found:
        soil = seed
    found = False
    for key in soil_fertilizer.keys():
        # print(f"{key=}")
        start, end = key
        if start <= soil <= end:
            fertilizer = soil_fertilizer[key][0] + (soil - start)
            found = True
            break
    if not found:
        fertilizer = soil
    found = False
    for key in fertilizer_water.keys():
        start, end = key
        if start <= fertilizer <= end:
            water = fertilizer_water[key][0] + (fertilizer - start)
            found = True
            break
    if not found:
        water = fertilizer
    found = False
    for key in water_light.keys():
        start, end = key
        if start <= water <= end:
            light = water_light[key][0] + (water - start)
            found = True
            break
    if not found:
        light = water
    found = False
    for key in light_temp.keys():
        start, end = key
        if start <= light <= end:
            temp = light_temp[key][0] + (light - start)
            found = True
            break
    if not found:
        temp = light
    found = False
    for key in temp_humidity.keys():
        start, end = key
        if start <= temp <= end:
            humidity = temp_humidity[key][0] + (temp - start)
            found = True
            break
    if not found:
        humidity = temp
    found = False
    for key in humidity_loc.keys():
        start, end = key
        if start <= humidity <= end:
            loc = humidity_loc[key][0] + (humidity - start)
            found = True
            break
    if not found:
        loc = humidity
    # print(f"{seed=}")
    # print(f"{soil=}")
    # print(f"{fertilizer=}")
    # print(f"{water=}")
    # print(f"{light=}")
    # print(f"{temp=}")
    # print(f"{humidity=}")
    # print(f"{loc=}")
    return loc

with open(file, 'rt') as f:
    separated_values = []
    lst = []
    all_lines = f.readlines()
    for i, line in enumerate(all_lines):
        if 'seeds:' not in line:
            lst.append(line.strip())
        if 'seeds:' in line:
            seeds = list(map(int, line[line.index(':') + 1:].strip().split()))
        if line == '\n' and lst[0] != '\n' and all(i.isnumeric() for i in line.split()):
            separated_values.append(lst)
            lst = []
        if i == len(all_lines) - 1:
            separated_values.append(lst)

del separated_values[0]

for i, lst in enumerate(separated_values):
    if i == 0:
        seed_soil = {(int(rng.split()[1]), int(rng.split()[1]) + int(rng.split()[2]) - 1):\
                     (int(rng.split()[0]), int(rng.split()[0]) + int(rng.split()[2]) - 1)
                     for j, rng in enumerate(lst) if j != 0 and lst[j] != ''}
    if i == 1:
        soil_fertilizer = {(int(rng.split()[1]), int(rng.split()[1]) + int(rng.split()[2]) - 1):\
                     (int(rng.split()[0]), int(rng.split()[0]) + int(rng.split()[2]) - 1)
                     for j, rng in enumerate(lst) if j != 0 and lst[j] != ''}
    if i == 2:
        fertilizer_water = {(int(rng.split()[1]), int(rng.split()[1]) + int(rng.split()[2]) - 1):\
                     (int(rng.split()[0]), int(rng.split()[0]) + int(rng.split()[2]) - 1)
                     for j, rng in enumerate(lst) if j != 0 and lst[j] != ''}
    if i == 3:
        water_light = {(int(rng.split()[1]), int(rng.split()[1]) + int(rng.split()[2]) - 1):\
                     (int(rng.split()[0]), int(rng.split()[0]) + int(rng.split()[2]) - 1)
                     for j, rng in enumerate(lst) if j != 0 and lst[j] != ''}
    if i == 4:
        light_temp = {(int(rng.split()[1]), int(rng.split()[1]) + int(rng.split()[2]) - 1):\
                     (int(rng.split()[0]), int(rng.split()[0]) + int(rng.split()[2]) - 1)
                     for j, rng in enumerate(lst) if j != 0 and lst[j] != ''}
    if i == 5:
        temp_humidity = {(int(rng.split()[1]), int(rng.split()[1]) + int(rng.split()[2]) - 1):\
                     (int(rng.split()[0]), int(rng.split()[0]) + int(rng.split()[2]) - 1)
                     for j, rng in enumerate(lst) if j != 0 and lst[j] != ''}
    if i == 6:
        humidity_loc = {(int(rng.split()[1]), int(rng.split()[1]) + int(rng.split()[2]) - 1):\
                     (int(rng.split()[0]), int(rng.split()[0]) + int(rng.split()[2]) - 1)
                     for j, rng in enumerate(lst) if j != 0 and lst[j] != ''}

print(f"Part 1: {min(find_location(seed) for seed in seeds)}")

part_2_seeds = []
for i in range(0, len(seeds), 2):
    if i < len(seeds) - 1:
        tup = (seeds[i], seeds[i] + seeds[i+1] - 1)
        part_2_seeds.append(tup)

print(f"Part 2: {min(find_location(seed) for rng in part_2_seeds for seed in range(rng[0], rng[1] + 1))}")