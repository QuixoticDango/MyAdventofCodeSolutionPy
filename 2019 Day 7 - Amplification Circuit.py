from itertools import permutations

class Amplifier():
    def __init__(self, intcode_computer, phase_setting, input_signal):
        self.halted = False
        self.pointer = 0
        self.computer = intcode_computer
        self.phase = phase_setting
        self.signal = input_signal

def parse_amplifiers(amp_list, code, id_lst):
    i = 0
    idx = 0
    while i < len(code):
        print(f"{i=}")
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
            # inp = int(input("Enter parameter: "))
            inp = id_lst[idx % 2]
            idx += 1
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
            return code[code[i-1]]

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

def parse_ampcode(code, id_lst):
    i = 0
    idx = 0
    while i < len(code):
        print(f"{i=}")
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
            # inp = int(input("Enter parameter: "))
            inp = id_lst[idx % 2]
            idx += 1
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
            return code[code[i-1]]

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

def run_setting(intcode, setting):
    output_from_last_amp = 0
    # ampcode = intcode.copy()
    for phase in setting:
        id_lst = [phase, output_from_last_amp]
        output_from_last_amp = parse_ampcode(intcode, id_lst)
    return int(output_from_last_amp)

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2019 Day 7 Advent of Code Input.txt"

with open(file, 'r') as f:
    amplifier_intcode = list(map(int, f.readline().strip().split(',')))

# print(max(run_setting(amplifier_intcode, setting) for setting in permutations(range(5))))

# Part 2
for phase_settings in permutations(range(5,10)):
    amplifiers = [Amplifier(amplifier_intcode, setting, 0) for setting in phase_settings]
    j = 0
    while not all(amplifiers[i].halted == True for i in range(len(amplifiers))):
        pass