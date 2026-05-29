def xmas_count(array):
    count = 0
    str1, str2, str3, str4, str5, str6, str7, str8 = '','','','','','','',''
    for i in range(len(array)):
        index = 0
        start = 0
        while index != -1:
            index = array[i].find('S', start)
            start = index + 1
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

file_path = "C:\\Users\\ANON\\Documents\\Coding and Programming Folder\\2024 Day 4 Advent of Code Input.txt"
array = [line.strip() for line in open(file_path,'r').readlines()]

print("The count is", xmas_count(array))
