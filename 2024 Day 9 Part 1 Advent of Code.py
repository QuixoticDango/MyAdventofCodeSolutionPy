import time

start = time.time()
def defragment(fragmented_disk):
    blocks = list(enumerate([fragmented_disk[i] for i in range(len(fragmented_disk)) if i % 2 == 0]))
    spaces = ['.' * int(fragmented_disk[i]) for i in range(len(fragmented_disk)) if i % 2 != 0]
    
    frag_disk_str = ''
    for i in range(len(blocks) * 2 - 1):
        if i % 2 == 0:
            frag_disk_str += str(blocks[i // 2][0]) * int(blocks[i // 2][1])
        else:
            frag_disk_str += spaces[(i - 1) // 2]

    num_file_blocks = 0
    for ch in frag_disk_str:
        if ch.isnumeric():
            num_file_blocks += 1
    
    check = False
    while not check:
        for i in range(-1, -len(frag_disk_str), -1):
            per_index = frag_disk_str.index('.')
            if frag_disk_str[i].isnumeric():
                frag_disk_str = frag_disk_str[:per_index] + frag_disk_str[i] + frag_disk_str[per_index+1:i] + '.' + frag_disk_str[-1:i:-1]
            else:
                continue
            check = all(frag_disk_str[k].isnumeric() for k in range(num_file_blocks))
            if check:
                break
    
    checkSum = 0
    for i in range(len(frag_disk_str)):
        if not frag_disk_str[i].isnumeric():
            break
        else:
            checkSum += int(frag_disk_str[i]) * i
    return checkSum

file_path = "C:\\Users\\ANON\\Documents\\Coding and Programming Folder\\2024 Day 9 Advent of Code Input.txt"
with open(file_path, 'r') as f:
    disk = [row.strip() for row in f.readline()]

print(defragment(disk))
end = time.time()

print("This program took", end - start, "seconds to run.")
