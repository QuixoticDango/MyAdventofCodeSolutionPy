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

file_path = "C:\\Users\\ANON\\Documents\\Coding and Programming Folder\\2024 Day 4 Advent of Code Input.txt"
array = [line.strip() for line in open(file_path,'r').readlines()]

print("The X-MAS count is", crossMascount(array))
