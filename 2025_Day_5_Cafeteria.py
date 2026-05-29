file = "C:\\Users\\DANGO\\Documents\\Coding and Programming Folder\\2025 Day 5 Advent of Code Input.txt"

with open(file, 'rt') as f:
    lines = f.readlines()
    fresh_ids = [tuple(map(int, line.strip().split('-'))) for line in lines if '-' in line]
    ids = [int(line.strip()) for line in lines if line != '\n' and '-' not in line]

total_num_of_fresh_ingredients = 0
for id in ids:
    for lower_bound, upper_bound in fresh_ids:
        if lower_bound <= id <= upper_bound:
            total_num_of_fresh_ingredients += 1
            break
print(total_num_of_fresh_ingredients)

fresh_ids.sort()

total_num_of_fresh_ids = 0
fresh_ids = [list(tup) for tup in fresh_ids]
while any(fresh_ids[m][1] >= fresh_ids[n][0] for m in range(len(fresh_ids) - 1) for n in range(m+1, len(fresh_ids))):
    for i, span in enumerate(fresh_ids):
        lb, ub = span
        j = i + 1
        while j < len(fresh_ids):
            if ub >= fresh_ids[j][0] - 1:
                if ub <= fresh_ids[j][1]:
                    fresh_ids[i][1] = fresh_ids[j][1]
                    del fresh_ids[j]
                else:
                    del fresh_ids[j]
            j += 1
total_num_of_fresh_ids = sum(ub - lb + 1 for lb, ub in fresh_ids)
print(total_num_of_fresh_ids)
