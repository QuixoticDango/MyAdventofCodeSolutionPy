file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 6 Advent of Code Input.txt"

with open(file) as f:
    i_pointer = 0
    f_pointer = i_pointer + 4
    f_p2 = i_pointer + 14
    stream = f.readline().strip()
    marker_loc = None
    marker_loc_2 = None
    found = False
    found_2 = False

    while f_pointer < len(stream):
        check_str = stream[i_pointer:f_pointer]
        check_str2 = stream[i_pointer:f_p2]
        if not found:
            if not any(check_str[i] == check_str[j] for i in range(len(check_str)-1)
                    for j in range(i+1, len(check_str))):
                marker_loc = f_pointer
                found = True
        
        if not found_2:
            if not any(check_str2[i] == check_str2[j] for i in range(len(check_str2)-1)
                    for j in range(i+1, len(check_str2))):
                marker_loc_2 = f_p2
                found_2 = True
        
        if found and found_2:
            break
            
        i_pointer += 1
        f_pointer += 1
        f_p2 += 1

print(f"Part 1: {marker_loc}")
print(f"Part 2: {marker_loc_2}")