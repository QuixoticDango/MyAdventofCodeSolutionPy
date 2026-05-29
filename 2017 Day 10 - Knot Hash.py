input_lengths = [70, 66, 255, 2, 48, 0, 54, 48, 80, 141, 244, 254, 160, 108, 1, 41]
# skip_size = 0
# loop = [i for i in range(256)]
# print(loop)
# position = 0

# for j, length in enumerate(input_lengths):
#     # if j != 0:
#     #     break
#     for i, n in enumerate(loop):
#         if length == 1:
#             continue
#         if i < length // 2:
#             loop[(i + position) % len(loop)], loop[(length + position - 1 - i) % len(loop)] = \
#                 loop[(length + position - 1 - i) % len(loop)], loop[(i + position) % len(loop)]
#     position += (length + skip_size) % len(loop)
#     skip_size += 1

# print(loop)
# print(f"Part 1: {loop[0] * loop[1]}")

# test_lengths = [3,4,1,5]
# test_skip = 0
# test_p = 0
# test_loop = [i for i in range(5)]
# for j, length in enumerate(test_lengths):
#     for i, n in enumerate(test_loop):
#         if i < length // 2:
#             test_loop[(i + test_p) % len(test_loop)], test_loop[(length + test_p - 1 - i) % len(test_loop)] = \
#                 test_loop[(length + test_p - 1 - i) % len(test_loop)], test_loop[(i + test_p) % len(test_loop)]
#     print(test_loop)
#     test_p += (length + test_skip) % len(loop)
#     test_skip += 1

# # print(test_loop)
# print(f"Part 1: {test_loop[0] * test_loop[1]}")

str_input = ','.join(list(map(str, input_lengths)))
print(str_input)

inputs = [ord(ch) for ch in str_input] + [17,31,73,47,23]
# print(inputs)

loop_2 = [i for i in range(256)]
skip_size = 0
position = 0
count = 0
while count < 64:
    for j, length in enumerate(input_lengths):
        for i, n in enumerate(loop_2):
            if length == 1:
                continue
            if i < length // 2:
                loop_2[(i + position) % len(loop_2)], loop_2[(length + position - 1 - i) % len(loop_2)] = \
                    loop_2[(length + position - 1 - i) % len(loop_2)], loop_2[(i + position) % len(loop_2)]
        position += (length + skip_size) % len(loop_2)
        skip_size += 1
    count += 1

sparse_hash = []
sub_list = []
for i, n in enumerate(loop_2, 1):
    sub_list.append(n)
    if i % 16 == 0:
        sparse_hash.append(sub_list)
        sub_list = []

# print(f"{loop_2 =}")
print(f"{sparse_hash =}")

dense_hash = []
for sublst in sparse_hash:
    xor_result = sublst[0]
    # print(f"{xor_result=}")
    for i, n in enumerate(sublst):
        if i == 15:
            print(f"{xor_result=}")
            dense_hash.append(xor_result)
            break
        xor_result ^= sublst[i + 1]

# print(f"{dense_hash=}")
# print(f"{len(dense_hash)=}")
# print(len(sparse_hash))

knot_hash = ''.join([str(hex(n))[2:] for n in dense_hash])
print(knot_hash)
# print(153^110^65^159^181^215^199^101^75^195^235^186^59^137^43^1)