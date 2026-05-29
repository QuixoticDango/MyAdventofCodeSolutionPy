file = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2025 Day 5 Advent of Code Input.txt"

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

# total_num_of_fresh_ids = len(set(n for lower_bound, upper_bound in fresh_ids for n in range(lower_bound, upper_bound+1)))

# fresh_ids.sort(key=lambda span: (span[0], span[1]))
# vector_ids = [(lower_bound, upper_bound - lower_bound) for lower_bound, upper_bound in fresh_ids]
print(f"Before = {len(fresh_ids)=}")
fresh_ids.sort(key=lambda span: (span[0], -span[1]))
# for i,id in enumerate(fresh_ids):
#     if id[0] == id[1]:
#         print(f"Row {i}: {id}")

lower_bounds = []
lower_bounds = [lower_bound for lower_bound, upperbound in fresh_ids if lower_bound not in lower_bounds]
lower_bounds.sort()
id_dict = {lower_bound:[] for lower_bound in lower_bounds}
for key in id_dict.keys():
    for id in fresh_ids:
        if id[0] == key:
            id_dict[key].append(id[1])
    id_dict[key].sort(reverse=True)

truncated_id_list = []
for key in id_dict:
    if len(id_dict[key]) > 1:
        print(f"{key}: {id_dict[key]}")
        id_dict[key] = id_dict[key][:1]
    truncated_id_list.append((key, id_dict[key][0]))
# print(truncated_id_list)

truncated_id_list.sort(key=lambda s: s[0])
truncated_id_list = [list(id) for id in truncated_id_list]
print(f"Before: {truncated_id_list=}")
truncated_id_list.sort(key=lambda s: (s[0], s[1]))

# truncated_id_list = [[lower_bound, upper_bound, False, True] for lower_bound, upper_bound in fresh_ids]
# new_spans = []
rounds = 0
# while any(truncated_id_list[m][2] or truncated_id_list[m][3] for m in range(len(truncated_id_list))):
#     if rounds == 0:
#         for id in truncated_id_list:
#             id[3] = False
    # if len(truncated_id_list) == 108:
    #     break
    # print("entered first while loop")
total_num_of_fresh_ids = 0
duplicates = False
while any(truncated_id_list[i][1] >= truncated_id_list[j][0] - 1 
          for i in range(len(truncated_id_list) - 1) 
          for j in range(i+1, len(truncated_id_list))):
    for i, span in enumerate(truncated_id_list):
        # print("entered for loop")
        lower_bound, upper_bound = span
        # if totally_overlapped:
        #     continue
        # if duplicates:
        #     duplicates = False
        #     continue
        if rounds == 0:
            if lower_bound == upper_bound:
                print('BOUNDS ARE EQUAL CONDITION')
                if 0 < i < len(truncated_id_list) - 1:
                    if lower_bound > truncated_id_list[i-1][1] and lower_bound < truncated_id_list[i+1][0]:
                        pass
                    else:
                        del truncated_id_list[i]
                        # duplicates = True
                        continue
                if i == 0 and lower_bound < truncated_id_list[i+1][0]:
                    pass
                elif i == len(truncated_id_list) - 1 and lower_bound > truncated_id_list[i-1][1]:
                    pass
                else:
                    del truncated_id_list[i]
                    # duplicates = True
                    continue
        k = i + 1
        while k < len(truncated_id_list):
            # print("entered jdsfa;lksdj;lfaskdjfsd while loop")
            print(f"{i=}")
            print(f"{k=}")
            # print(f"{len(truncated_id_list)=}")
            if upper_bound >= truncated_id_list[k][0] - 1:
                # print("reached first condition")
                if upper_bound >= truncated_id_list[k][1]:
                    del truncated_id_list[k]
                    k -= 1
                else:
                    # print("reached else")
                    truncated_id_list[i][1] = truncated_id_list[k][1]
                    del truncated_id_list[k]
                    k -= 1
            
            # else:
            #     truncated_id_list[k][2] = truncated_id_list[k][3] = False
            k += 1
        # print(truncated_id_list)
        # print(f"{any(truncated_id_list[i][1] >= truncated_id_list[j][0] - 1 
        #   for i in range(len(truncated_id_list)) 
        #   for j in range(i+1, len(truncated_id_list)))=}")
    rounds += 1

# print(fresh_ids)
# print(any(fresh_ids[m][2] or fresh_ids[m][3] for m in range(len(fresh_ids))))
# for h, d in enumerate(fresh_ids):
#     i,j,k,l = d
#     if k or l:
#         print(f"Index: {h} and span: {i=}, {j=}")
# print(f"After = {len(fresh_ids)=}")

for l, u in truncated_id_list:
    total_num_of_fresh_ids += u - l + 1
    print(f"{l}, {u}")
print(f"Final ID list: {truncated_id_list}")
print(f"{len(truncated_id_list)=}")
print(f"{total_num_of_fresh_ids=}")

# truncated_id_list[i][1] >= truncated_id_list[j][0] - 1 
# for i in range(len(truncated_id_list) - 1):
#     for j in range(i+1, len(truncated_id_list)):

# # total_num_of_fresh_ids = sum(upper_bound - lower_bound + 1 for lower_bound, upper_bound, s, t in fresh_ids)
# # for i, span in enumerate(fresh_ids):
# #     if i == len(fresh_ids) - 1:
# #         break
# #     lower_bound, upper_bound = span
# #     total_num_of_fresh_ids += (fresh_ids[i+1][1] - fresh_ids[i+1][0]) - (upper_bound - lower_bound)

# # if len(fresh_ids) % 2 == 1:
# #     last_id = fresh_ids[-1]
# #     fresh_ids = fresh_ids[:-1]
# #     odd_num_ids = True
# # print(f"Sorted ids: {fresh_ids}")
# # this_span_overlaps_previous_span = False
# # check = 0
# # total_num_of_fresh_ids = 0
# # for i, span in enumerate(fresh_ids):
# #     overlaps = 0
# #     if this_span_overlaps_previous_span and i == len(fresh_ids) - 1:
# #         print("reached first break condition")
# #         # check = 1
# #         break
# #     if not this_span_overlaps_previous_span and i == len(fresh_ids) - 1:
# #         print("reached second break condition")
# #         # check = 2
# #         lower_bound, upper_bound = span
# #         total = upper_bound - lower_bound + 1
# #         total_num_of_fresh_ids += total
# #         break
# #     if this_span_overlaps_previous_span:
# #         this_span_overlaps_previous_span = False
# #         continue

# #     lower_bound, upper_bound = span
# #     k = i+1
# #     while upper_bound < fresh_ids[i+1][0] - 1 and k < len(fresh_ids) - 1:
# #         overlaps += 1
# #         total = upper_bound - lower_bound + 1
# #         total_num_of_fresh_ids += total
# #         k += 1
# #     else:
# #         total = fresh_ids[i+1][1] - lower_bound + 1
# #         total_num_of_fresh_ids += total
# #         this_span_overlaps_previous_span = True

# # if this_span_overlaps_previous_span:
# #     total_num_of_fresh_ids += fresh_ids[-1][1] - fresh_ids[-2][0] + 1
# # print(fresh_ids)
# # # 1. No overlap between spans - i.e. upper bound of first span is less than lower bound of second span minus 1.
# # #    If there's no overlap, sum the elements of current list and continue loop as usual.
# # # 2. Overlap between spans - i.e. upper bound of first span is equal to or greater than lower bound of second span minus 1.
# # #    If there's overlap, sum the elements using the upper bound of the second span and the lower of the first. Skip the next
# # #    span.
# # print(total_num_of_fresh_ids)
