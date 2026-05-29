def parse_code(code):
    i = 0
    while i < len(code):
        # print(f"{i=}")
        if code[i] == '1':
            one = int(code[int(code[i+1])])
            two = int(code[int(code[i+2])])
            three = int(code[i+3])
            code[three] = str(one + two)
            i += 4
            # print(f"{i=}")
            # print(f"{code[i]=}")
            # print(f"{one=}")
            # print(f"{two=}")
            # print(f"{three=}")
            # print(f"{code[three]=}")
            continue
        if code[i] == '2':
            one = int(code[int(code[i+1])])
            two = int(code[int(code[i+2])])
            three = int(code[i+3])
            code[three] = str(one * two)
            i += 4
            # print(f"{i=}")
            # print(f"{code[i]=}")
            # print(f"{one=}")
            # print(f"{two=}")
            # print(f"{three=}")
            # print(f"{code[three]=}")
            continue
        if code[i] == '3':
            ID = input("Enter value: ")
            code[int(code[i+1])] = ID
            print(f"{code[int(code[i+1])]=}")
            i += 2
            continue
        if code[i] == '4':
            print(f"Reached parameter 4: {code[int(code[i+1])]}")
            i += 2
            continue
        if code[i] == '5':
            one = int(code[int(code[i+1])])
            two = int(code[int(code[i+2])])
            if one != 0:
                i = two
                # print(f"{i=}")
                # print(f"{code[i]=}")
                # # print(f"{parameters=}")
                # print(f"{one=}")
                # print(f"{two=}")
                # print(f"{three=}")
                # print(f"{code[three]=}")
                continue
            else:
                i += 1
                # print(f"{i=}")
                # print(f"{code[i]=}")
                # # print(f"{parameters=}")
                # print(f"{one=}")
                # print(f"{two=}")
                # print(f"{three=}")
                # print(f"{code[three]=}")
                continue
        if code[i] == '6':
            one = int(code[int(code[i+1])])
            two = int(code[int(code[i+2])])
            if one == 0:
                i = two
                # print(f"{i=}")
                # print(f"{code[i]=}")
                # # print(f"{parameters=}")
                # print(f"{one=}")
                # print(f"{two=}")
                # print(f"{three=}")
                # print(f"{code[three]=}")
                continue
            else:
                i += 1
                # print(f"{i=}")
                # print(f"{code[i]=}")
                # # print(f"{parameters=}")
                # print(f"{one=}")
                # print(f"{two=}")
                # print(f"{three=}")
                # print(f"{code[three]=}")
                continue
        if code[i] == '7':
            one = int(code[int(code[i+1])])
            two = int(code[int(code[i+2])])
            three = int(code[i+3])
            if one < two:
                code[three] = '1'
                i += 4
                # print(f"{i=}")
                # print(f"{code[i]=}")
                # # print(f"{parameters=}")
                # print(f"{one=}")
                # print(f"{two=}")
                # print(f"{three=}")
                # print(f"{code[three]=}")
                continue
            else:
                code[three] = '0'
                i += 4
                # print(f"{i=}")
                # print(f"{code[i]=}")
                # # print(f"{parameters=}")
                # print(f"{one=}")
                # print(f"{two=}")
                # print(f"{three=}")
                # print(f"{code[three]=}")
                continue
        if code[i] == '8':
            one = int(code[int(code[i+1])])
            two = int(code[int(code[i+2])])
            three = int(code[i+3])
            if one == two:
                code[three] = '1'
                i += 4
                # print(f"{i=}")
                # print(f"{code[i]=}")
                # # print(f"{parameters=}")
                # print(f"{one=}")
                # print(f"{two=}")
                # print(f"{three=}")
                # print(f"{code[three]=}")
                continue
            else:
                code[three] = '0'
                i += 4
                # print(f"{i=}")
                # print(f"{code[i]=}")
                # # print(f"{parameters=}")
                # print(f"{one=}")
                # print(f"{two=}")
                # print(f"{three=}")
                # print(f"{code[three]=}")
                continue
        if code[i] == '99':
            return 0
        
        if len(code[i]) > 2:
            if len(code[i]) < 5:
                code[i] = '0' * (5 - len(code[i])) + code[i]
            if not all(ch == '1' or ch == '0' for ch in code[i][:3]):
                i += 1
                continue
            mode = code[i][3:]
            parameters = code[i][:3]
            try:
                param_1 = parameters[2]
            except IndexError:
                param_1 = '0'
                continue
            try:
                param_2 = parameters[1]
            except IndexError:
                param_2 = '0'
            try:
                param_3 = parameters[0]
            except IndexError:
                param_3 = '0'
            
            if mode == '01':
                if param_1 == '0':
                    one = int(code[int(code[i+1])])
                if param_1 == '1':
                    one = int(code[i+1])
                if param_2 == '0':
                    two = int(code[int(code[i+2])])
                if param_2 == '1':
                    two = int(code[i+2])
                three = int(code[i+3])
                
                code[three] = str(one + two)
                i += 4
                # print(f"{i=}")
                # print(f"{code[i]=}")
                # print(f"{parameters=}")
                # print(f"{one=}")
                # print(f"{two=}")
                # print(f"{three=}")
                # print(f"{code[three]=}")
                continue

            if mode == '02':
                if param_1 == '0':
                    one = int(code[int(code[i+1])])
                if param_1 == '1':
                    one = int(code[i+1])
                if param_2 == '0':
                    two = int(code[int(code[i+2])])
                if param_2 == '1':
                    two = int(code[i+2])
                three = int(code[i+3])

                code[three] = str(one * two)
                i += 4
                # print(f"{i=}")
                # print(f"{code[i]=}")
                # print(f"{parameters=}")
                # print(f"{one=}")
                # print(f"{two=}")
                # print(f"{three=}")
                # print(f"{code[three]=}")
                continue

            if mode == '05':
                # print('MODE 5')
                # print('=' * 10)
                if param_1 == '0':
                    one = int(code[int(code[i+1])])
                if param_1 == '1':
                    one = int(code[i+1])
                if param_2 == '0':
                    two = int(code[int(code[i+2])])
                if param_2 == '1':
                    two = int(code[i+2])
                # print(f"THIS IS WHAT ONE IS = {one}")
                if one != 0:
                    # print(f"{i=}")
                    # print(f"{code[i]=}")
                    # print(f"{code[i+1]=}")
                    # print(f"{code[i+2]=}")
                    # print(f"{parameters=}")
                    # print(f"{one=}")
                    # print(f"{two=}")
                    # print(f"{code[two]=}")
                    i = two
                    # print(f"AFTER assignment: {i=}")
                    continue
                else:
                    i += 1
                    # print(f"{i=}")
                    # print(f"{code[i]=}")
                    # print(f"{parameters=}")
                    # print(f"{one=}")
                    # print(f"{two=}")
                    # print(f"{three=}")
                    # print(f"{code[three]=}")
                    continue
                
            if mode == '06':
                # print('MODE 6')
                # print('=' * 10)
                if param_1 == '0':
                    one = int(code[int(code[i+1])])
                if param_1 == '1':
                    one = int(code[i+1])
                if param_2 == '0':
                    two = int(code[int(code[i+2])])
                if param_2 == '1':
                    two = int(code[i+2])

                if one == 0:
                    # print(f"{i=}")
                    # print(f"{code[i]=}")
                    # print(f"{parameters=}")
                    # print(f"{one=}")
                    # print(f"{two=}")
                    # print(f"{three=}")
                    # print(f"{code[three]=}")
                    i = two
                    continue
                else:
                    i += 1
                    # print(f"{i=}")
                    # print(f"{code[i]=}")
                    # print(f"{parameters=}")
                    # print(f"{one=}")
                    # print(f"{two=}")
                    # print(f"{three=}")
                    # print(f"{code[three]=}")
                    continue
            
            if mode == '07':
                # print('pMODE 7')
                # print('=' * 10)
                if param_1 == '0':
                    one = int(code[int(code[i+1])])
                if param_1 == '1':
                    one = int(code[i+1])
                if param_2 == '0':
                    two = int(code[int(code[i+2])])
                if param_2 == '1':
                    two = int(code[i+2])
                three = int(code[i+3])
            
                if one < two:
                    code[three] = '1'
                    i += 4
                    # print(f"{i=}")
                    # print(f"{code[i]=}")
                    # print(f"{parameters=}")
                    # print(f"{one=}")
                    # print(f"{two=}")
                    # print(f"{three=}")
                    # print(f"{code[three]=}")
                    continue
                else:
                    code[three] = '0'
                    i += 4
                    # print(f"{i=}")
                    # print(f"{code[i]=}")
                    # print(f"{parameters=}")
                    # print(f"{one=}")
                    # print(f"{two=}")
                    # print(f"{three=}")
                    # print(f"{code[three]=}")
                    continue
            
            if mode == '08':
                # print('MODE 8')
                # print('=' * 10)
                if param_1 == '0':
                    one = int(code[int(code[i+1])])
                if param_1 == '1':
                    one = int(code[i+1])
                if param_2 == '0':
                    two = int(code[int(code[i+2])])
                if param_2 == '1':
                    two = int(code[i+2])
                three = int(code[i+3])
            
                if one == two:
                    code[three] = '1'
                    i += 4
                    # print(f"{i=}")
                    # print(f"{code[i]=}")
                    # print(f"{parameters=}")
                    # print(f"{one=}")
                    # print(f"{two=}")
                    # print(f"{three=}")
                    # print(f"{code[three]=}")
                    continue
                else:
                    code[three] = '0'
                    i += 4
                    # print(f"{i=}")
                    # print(f"{code[i]=}")
                    # print(f"{parameters=}")
                    # print(f"{one=}")
                    # print(f"{two=}")
                    # print(f"{three=}")
                    # print(f"{code[three]=}")
                    continue
        i += 1

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2019 Day 5 Advent of Code Input.txt"

stream = open(file, 'rt')
intcode = stream.read().strip().split(',')
stream.close()

parse_code(intcode)