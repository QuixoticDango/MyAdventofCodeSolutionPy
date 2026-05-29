import time

start = time.time()
# def defragment(fragmented_disk):
#     blocks = list(enumerate([fragmented_disk[i] for i in range(len(fragmented_disk)) if i % 2 == 0]))
#     spaces = ['.' * int(fragmented_disk[i]) for i in range(len(fragmented_disk)) if i % 2 != 0]
    
#     frag_disk_str = ''
#     for i in range(len(blocks) * 2 - 1):
#         if i % 2 == 0:
#             frag_disk_str += str(blocks[i // 2][0]) * int(blocks[i // 2][1])
#         else:
#             frag_disk_str += spaces[(i - 1) // 2]

#     num_file_blocks = 0
#     for ch in frag_disk_str:
#         if ch.isnumeric():
#             num_file_blocks += 1
    
#     check = False
#     while not check:
#         for i in range(-1, -len(frag_disk_str), -1):
#             per_index = frag_disk_str.index('.')
#             if frag_disk_str[i].isnumeric():
#                 frag_disk_str = frag_disk_str[:per_index] + frag_disk_str[i] + frag_disk_str[per_index+1:i] + '.' + frag_disk_str[-1:i:-1]
#             else:
#                 continue
#             # print(f"{frag_disk_str=}")
#             # time.sleep(1)
#             check = all(frag_disk_str[k].isnumeric() for k in range(num_file_blocks))
#             if check:
#                 break
    
#     checkSum = 0
#     for i in range(len(frag_disk_str)):
#         if not frag_disk_str[i].isnumeric():
#             break
#         else:
#             checkSum += int(frag_disk_str[i]) * i
#     return checkSum

def defragment2(string):

    blocks = list(enumerate([string[i] for i in range(len(string)) if i % 2 == 0]))
    spaces = ['.' * int(string[i]) for i in range(len(string)) if i % 2 != 0]
    
    frag_disk_str = ''
    for i in range(len(blocks) * 2 - 1):
        if i % 2 == 0:
            frag_disk_str += str(blocks[i // 2][0]) * int(blocks[i // 2][1])
        else:
            frag_disk_str += spaces[(i - 1) // 2]
    
    print(f"{frag_disk_str=}")

    
    digitNum = sum(1 for i in range(len(frag_disk_str)) if frag_disk_str[i].isnumeric())
    for i in range(digitNum):    
        if not frag_disk_str[i].isnumeric():
            last_dot_i = i - len(frag_disk_str)
    fillDotNum = sum(1 for i in range(last_dot_i+len(frag_disk_str)) if frag_disk_str[i] == '.') + 1
    print(f"{last_dot_i=}")
    print(f"{fillDotNum=}")

    for i in range(last_dot_i + len(frag_disk_str) + 1, len(frag_disk_str)):
        if frag_disk_str[i].isnumeric():
            last_num_i = i
            break
    print(f"{last_num_i=}")

    checkSum = 0
    start = 0
    count = 0
    print(f"{frag_disk_str[-1]=}",
          f"{frag_disk_str[-2]=}")
    for i in range(last_num_i):
        if frag_disk_str[i].isnumeric():
            # print(f"Reached 'if' on {i=} and {frag_disk_str[i]=}")
            checkSum += int(frag_disk_str[i]) * i
            # print(f"{checkSum=} after first 'for' loop.")
        else:
            check = False
            while count < fillDotNum:            
                if check:
                    break
                count += 1
                # print(f"Reached 'else' on {i=} and {frag_disk_str[i]=}")
                for j in range(-1 + start, -len(frag_disk_str), -1):
                    if frag_disk_str[j].isnumeric():
                        # print(f"{i=} in second 'for' loop.")
                        # print(f"{frag_disk_str[j]=} in second 'for' loop.")
                        checkSum += i * int(frag_disk_str[j])
                        # print(f"{checkSum=} after second 'for' loop.")
                        start = j
                        # print(f"{start=}")
                        # print(f"{count=}")
                        if count > 0:
                            check = True
                            break
    print(f"{frag_disk_str[last_num_i]=}")
    checkSum += int(frag_disk_str[last_num_i]) * (last_dot_i + len(frag_disk_str))
    return checkSum


file_path = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2024 Day 9 Advent of Code Input Test.txt"
with open(file_path, 'r') as f:
    disk = f.readline().strip()

print(defragment2(disk))
end = time.time()

print("This program took", end - start, "seconds to run.")