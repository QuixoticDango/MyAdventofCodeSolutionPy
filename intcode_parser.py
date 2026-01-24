def parse_code(code):
    i = 0
    while i < len(code):
        if code[i] == 1:
            one = code[code[i+1]]
            two = code[code[i+2]]
            three = code[i+3]
            code[three] = one + two
            i += 4
            continue
        
        if code[i] == 2:
            one = code[code[i+1]]
            two = code[code[i+2]]
            three = code[i+3]
            code[three] = one * two
            i += 4
            continue
        
        if code[i] == 3:
            inp = int(input("Enter parameter: "))
            address = code[i+1]
            code[address] = inp
            i += 2
            continue
        
        if code[i] == 4:
            print(f"Reached parameter 4: {code[code[i+1]]}")
            i += 2
            continue
        
        if code[i] == 5:
            if code[i+1] != 0:
                i = code[i+2]
            else:
                i += 1
            continue

        if code[i] == 6:
            if code[i+1] == 0:
                i = code[i+2]
            else:
                i += 1
            continue

        if code[i] == 7:
            if code[i+1] < code[i+2]:
                code[code[i+3]] = 1
            else:
                code[code[i+3]] = 0
            
            i += 4
            continue
    
        if code[i] == 8:
            if code[i+1] == code[i+2]:
                code[code[i+3]] = 1
            else:
                code[code[i+3]] = 0
            
            i += 4
            continue

        if code[i] == 99:
            return 0

        if len(str(code[i])) > 2:
            str_code = str(code[i])
            if len(str_code) < 5:
                str_code = '0' * (5 - len(str_code)) + str_code

            if all(ch == '1' or ch == '0' for ch in str_code[:3]):
                mode = str_code[3:]
                param_3, param_2, param_1 = str_code[:3]

                if mode == '01':
                    if param_1 == '0':
                        one = code[code[i+1]]
                    if param_1 == '1':
                        one = code[i+1]
                    if param_2 == '0':
                        two = code[code[i+2]]
                    if param_2 == '1':
                        two = code[i+2]
                    three = code[i+3]
                    code[three] = one + two

                    i += 4
                    continue
                
                if mode == '02':
                    if param_1 == '0':
                        one = code[code[i+1]]
                    if param_1 == '1':
                        one = code[i+1]
                    if param_2 == '0':
                        two = code[code[i+2]]
                    if param_2 == '1':
                        two = code[i+2]
                    three = code[i+3]
                    code[three] = one * two

                    i += 4
                    continue
                
                if mode == '05':
                    if param_1 == '0':
                        one = code[code[i+1]]
                    if param_1 == '1':
                        one = code[i+1]
                    if param_2 == '0':
                        two = code[code[i+2]]
                    if param_2 == '1':
                        two = code[i+2]

                    if one != 0:
                        i = two
                    else:
                        i += 1
                    continue

                if mode == '06':
                    if param_1 == '0':
                        one = code[code[i+1]]
                    if param_1 == '1':
                        one = code[i+1]
                    if param_2 == '0':
                        two = code[code[i+2]]
                    if param_2 == '1':
                        two = code[i+2]

                    if one == 0:
                        i = two
                    else:
                        i += 1
                    continue

                if mode == '07':
                    if param_1 == '0':
                        one = code[code[i+1]]
                    if param_1 == '1':
                        one = code[i+1]
                    if param_2 == '0':
                        two = code[code[i+2]]
                    if param_2 == '1':
                        two = code[i+2]
                    three = code[i+3]

                    if one < two:
                        code[three] = 1
                    else:
                        code[three] = 0
                    
                    i += 4
                    continue
                
                if mode == '08':
                    if param_1 == '0':
                        one = code[code[i+1]]
                    if param_1 == '1':
                        one = code[i+1]
                    if param_2 == '0':
                        two = code[code[i+2]]
                    if param_2 == '1':
                        two = code[i+2]
                    three = code[i+3]

                    if one == two:
                        code[three] = 1
                    else:
                        code[three] = 0
                    
                    i += 4
                    continue
        
        i += 1

if __name__ == "__main__":
    file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2019 Day 5 Advent of Code Input.txt"

    with open(file, 'rt') as f:
        intcode = list(map(int, f.readline().strip().split(',')))

    parse_code(intcode)
