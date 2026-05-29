def xmas_count(array):
    count = 0
    str1, str2, str3, str4, str5, str6, str7, str8 = '','','','','','','',''
    for i in range(len(array)):
        index = 0
        start = 0
        while index != -1:
            index = array[i].find('S', start)
            if index == -1:
                break
            start = index + 1
            print(f"{index=} {start=}")
            # Scan forward for XMAS within row   
            if len(array[i]) - index > 3:
                str1 = ''
                scan = 0
                while scan < 4:
                    str1 += array[i][index + scan]
                    scan += 1
                if str1 == 'SAMX':
                    count += 1
            # Scan backward within row
            if index >= 3:
                    str2 = ''
                    scan = 0
                    while scan < 4:
                        str2 += array[i][index - scan]
                        scan += 1
                    if str2 == 'SAMX':
                        count += 1
            # Scan up for XMAS within column
            if i >= 3:
                str3 = ''
                scan = 0
                while scan < 4:
                    str3 += array[i - scan][index]
                    scan += 1
                if str3 == "SAMX":
                    count += 1
            # Scan down within column
            if len(array) - i > 3:
                str4 = ''
                scan = 0
                while scan < 4:
                    str4 += array[i + scan][index]
                    scan += 1
                if str4 == "SAMX":
                    count += 1
            # Scan forward and up
            if len(array[i]) - index > 3 and i >= 3:
                str5 = ''
                scan = 0
                while scan < 4:
                    str5 += array[i - scan][index + scan]
                    scan += 1
                if str5 == 'SAMX':
                    count += 1
            # Scan forward and down
            if len(array[i]) - index > 3 and len(array) - i > 3:
                str6 = ''
                scan = 0
                while scan < 4:
                    str6 += array[i + scan][index + scan]
                    scan += 1
                if str6 == "SAMX":
                    count += 1
            # Scan backward and up
            if index >= 3 and i >= 3:
                str7 = ''
                scan = 0
                while scan < 4:
                    str7 += array[i - scan][index - scan]
                    scan += 1
                if str7 == "SAMX":
                    count += 1
            # Scan backward and down
            if index >= 3 and len(array) - i > 3:
                str8 = ''
                scan = 0
                while scan < 4:
                    str8 += array[i + scan][index - scan]
                    scan += 1
                if str8 == "SAMX":
                    count += 1
    return count

def crossMascount(array):
    acceptable = ('AMSMS', 'AMMSS', 'ASMSM', 'ASSMM')
    count = 0
    for i in range(len(array)):
        index = 0
        start = 0
        try:
            while index != -1:
                index = array[i].find('A', start)
                start = index + 1
                Xstring = array[i][index] + array[i-1][index-1] + array[i-1][index+1] \
                    + array[i+1][index-1] + array[i+1][index+1]
                if Xstring in acceptable:
                    count += 1
        except:
            continue
    return count

file_path = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2024 Day 4 Advent of Code Input Test.txt"
array = [line.strip() for line in open(file_path,'r').readlines()]

print("The X-MAS count is", xmas_count(array))

# import re

# def count_xmas(i_content):
#     if len(re.findall('MAS',i_content)) != 0 or len(re.findall('MAS',i_content[::-1])) != 0:
#         return True

# file_path = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2024 Day 4 Advent of Code Input.txt"
# file = [ line.strip() for line in open(file_path,'r').readlines() ]
# summa = 0

# for index, value in enumerate(file):
    
#     if index == 0: continue
# # Find all occurences
#     all_occ = re.finditer('A',value)

# #  Loop on all find cases
#     for match in all_occ:
#         if match.start() == 0: continue
#         try:
#             prev_row = file[index - 1]
#             next_row = file[index + 1]
#     #       Left up + middle + right bottom
#             string_leftup = prev_row[match.start() - 1] + file[index][match.start()] + next_row[match.start() + 1]
#     #       Left down + middle + right up
#             string_rightup = next_row[match.start() - 1] + file[index][match.start()] + prev_row[match.start() + 1]

#             summa = summa + 1 if count_xmas(string_leftup) == True and count_xmas(string_rightup) == True else summa
#         except: continue
# print(summa)

# import re

# def count_xmas(i_content):
#     global summa
#     summa += len(re.findall('XMAS',i_content)) + len(re.findall('XMAS',i_content[::-1]))

# def rotate_by_45(array, direction):
#     rotated_array = []
#     row_index = 0
# #   Convert first line to first col in new array from n. index 
#     for index, i in enumerate(array):
#         row_index = index
#         for j in i if direction == 'R' else i[::-1]:
#             try:
#                 rotated_array[row_index][0] = j + rotated_array[row_index][0] if direction == 'R' else rotated_array[row_index][0] + j  
#             except: 
#                 rotated_array.append([j]) 
#             row_index += 1
#     return rotated_array

# file_path = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2024 Day 4 Advent of Code Input.txt"
# file = [ line.strip() for line in open(file_path,'r').readlines() ]
# summa = 0
# position_index = 0

# # Vertical
# while True:
#     try: 
# #   Get all columns next to next, and convert to single string 
#         col_content = ''.join( [ i[position_index] for i in file ] )
#     except: break

# #   Count XMAS string in proper string in both way    
#     count_xmas(col_content)
#     position_index += 1

# # Horizontal
# # Get all columns next to next, and convert to single string
# for i in file:    
# #   Count XMAS string in proper string in both way    
#     count_xmas(i)
        
# # Diagonal
# #  Rotate right
# rotated_array = rotate_by_45(file,'R')
# for i in rotated_array:
#     count_xmas(str(i))
    
# #  Rotate left
# rotated_array = rotate_by_45(file,'L')
# for i in rotated_array:
#     count_xmas(str(i))
    
# print(summa)