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

def find_next_step(item_rang, id):
    item_start, item_end = item_rang
    if id == 'seed':
        start_is_in_range = False
        end_is_in_range = False
        soil_ranges = []
        found = False
        for key in seed_soil.keys():
            start, end = key
            if start <= item_start <= end:
                soil_start = seed_soil[key][0] + (item_start - start)
                start_is_in_range = True
                break
        for key in seed_soil.keys():
            start, end = key
            if start <= item_end <= end:
                soil_end = seed_soil[key][0] + (item_end - start)
                end_is_in_range = True
                break
        if start_is_in_range and end_is_in_range:
            soil_ranges.append((soil_start, soil_end))
            return soil_ranges
        if not start_is_in_range and end_is_in_range:
            key_list = list(seed_soil.keys())
            key_list.sort(key=lambda s: s[0])
            min_start_range = key_list[0]
            soil_ranges.append((item_start, min_start_range[0] - 1))
            soil_ranges.append((seed_soil[min_start_range][0],
                                seed_soil[min_start_range][0] + (item_end - min_start_range[0])))
        if start_is_in_range and not end_is_in_range:
            key_list = list(seed_soil.keys())
            key_list.sort(key=lambda s: s[0])
            min_start_range = key_list[0]
            soil_ranges.append((item_start, min_start_range[0] - 1))
            soil_ranges.append((seed_soil[min_start_range][0],
                                seed_soil[min_start_range][0] + (item_end - min_start_range[0])))

def is_in_range(n, rang):
    start, end = rang
    if start <= n <= end:
        return True
    return False

def find_next_range(ranges, category):
    sources = list(category.keys())
    sources.sort(key=lambda m: m[0])
    gap_ranges = []
    gap_loc = []
    filled_ranges = []
    for i, s in enumerate(sources):
        start, end = s
        if i + 1 < len(sources):
            if sources[i+1][0] - end > 1:
                filled_ranges.append((sources[0][0], end))
                gap_ranges.append((end + 1, sources[i+1][0] - 1))
                gap_loc.append(i)
        if i == len(sources) - 1:
            filled_ranges.append((gap_ranges[-1][1] + 1, end))

    dest = []
    range_is_gap_adjacent = False
    start_is_in_gap = False
    end_is_in_gap = False
    # bound_is_in_total_range = False
    range_straddles_gap = False
    for i, r in enumerate(ranges):
        range_completed = False
        bound_is_in_total_range = True
        start, end = r
        if start < sources[0][0]:
            dest.append((start, sources[0][0] - 1))
        if end > sources[-1][0]:
            dest.append((sources[-1][0] + 1, end))
        start_range_loc = -len(sources) - 1
        end_range_loc = -len(sources) - 1
        for j, source in enumerate(sources):
            s_start, s_end = source
            if s_start <= start <= s_end:
                start_range_loc = j
            if s_start <= end <= s_end:
                end_range_loc = j
            if start_range_loc
            # Start and end within single source range
            if s_start <= start <= s_end and s_start <= end <= s_end:
                new_start = category[source][0] + (start - s_start)
                new_end = category[source][0] + (end - s_start)
                dest.append((new_start, new_end))






        bound_is_in_total_range = False
        both_bounds_are_mapped = False
        start, end = r
        if sources[0][0] <= start <= sources[-1][1] or sources[0][0] <= end <= sources[-1][1]:
            bound_is_in_total_range = True
        if any(filled_range[0] <= start <= filled_range[1] for filled_range in filled_ranges) and \
            any(filled_range[0] <= start <= filled_range[1] for filled_range in filled_ranges):
            both_bounds_are_mapped = True
            if any(start < gap_range[0] and end > gap_range[1] for gap_range in gap_ranges)

        for j, rang in enumerate(sources):
            for gap in gap_ranges:
                if not any(ran[0] <= start <= ran[1] for ran in sources):
                        start_is_in_gap = True
                if not any(ran[0] <= end <= ran[1] for ran in sources):
                        end_is_in_gap = True
                if rang[0] - 1 == gap[1] or rang[1] + 1 == gap[0]:
                    adjacent_gap = gap
                    range_is_gap_adjacent = True
                    break
            # left overlap with start in adjacent gap
            if start < rang[0] and rang[0] <= end <= rang[1] and range_is_gap_adjacent:
                dest.append((start, rang[0] - 1))
                new_start = category[rang][0]
                new_end = category[rang][0] + (end - rang[0])
                dest.append((new_start, new_end))
            # complete overlap
            if rang[0] <= start <= rang[1] and rang[0] <= end <= rang[1]:
                new_start = category[rang][0] + (start - rang[0])
                new_end = category[rang][0] + (end - rang[0])
                dest.append((new_start, new_end))
            # right overlap
            if rang[0] <= start <= rang[1] and rang[1] > end:
                dest.append((rang[1] + 1, end))
                new_start = category[rang][0]
                new_end = category[rang][0] + (end - rang[0])
                dest.append((new_start, new_end))
# def consolidate_ranges(category):
#     sources = list(category.keys())
#     dest = list(category.values())
#     sources.sort(key=lambda k: k[0])
#     dest.sort(key=lambda k: k[0])

#     there_is_an_overlap = True
#     while there_is_an_overlap:
#         there_is_an_overlap = False
#         for i, s in enumerate(sources):
#             s_start, s_end = s
#             d_start, d_end = category[s]
#             s_next_start, s_next_end = sources[i+1]
#             d_next_start, d_next_end = category[sources[i+1]]
#             if i + 1 < len(sources):
#                 if s_end > s_next_start:


# def map_ranges(s_rang):
#     for s_ran in 

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

# part_2_seeds = []
# for i in range(0, len(seeds), 2):
#     if i < len(seeds) - 1:
#         tup = (seeds[i], seeds[i] + seeds[i+1] - 1)
#         part_2_seeds.append(tup)

# print(f"Part 2: {min(find_location(seed) for rng in part_2_seeds for seed in range(rng[0], rng[1] + 1))}")

# seed_ranges = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]
# for ran in seed_ranges:
# print(seed_soil)
lst = [[key, water_light[key]] for key in water_light.keys()]
lst.sort(key=lambda n: n[0][0])
# print(lst)
for i, x in enumerate(lst):
    s, d = x
    print(s)
    if i+1 < len(lst):
        if lst[i+1][0][0] - s[1] > 1:
            print(f"GAP: {lst[i+1][0][0] - s[1]}")