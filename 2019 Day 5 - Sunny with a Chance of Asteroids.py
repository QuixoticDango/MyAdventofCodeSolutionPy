# def parse_code(code):
#     i = 0
#     while i < len(code):
#         print(f"{i=}")
#         print(f"{code[-672]=}")
#         # print(f"{len(code)=}")
#         if code[i] == '1':
#             code[int(code[i+3])] = str(int(code[int(code[i+1])]) + int(code[int(code[i+2])]))
#             i += 4
#             continue
#         if code[i] == '2':
#             code[int(code[i+3])] = str(int(code[int(code[i+1])]) * int(code[int(code[i+2])]))
#             i += 4
#             continue
#         if code[i] == '3':
#             ID = input("Enter value: ")
#             code[int(code[i+1])] = ID
#             i += 2
#             continue
#         if code[i] == '4':
#             print(code[int(code[i+1])])
#             i += 2
#             continue
#         if code[i] == '99':
#             print(f"{code[i]=}")
#             return -1
        
#         if len(code[i]) > 1 and all(ch == '1' or ch == '0' for ch in code[i]):
#             mode = code[i][-2:]
#             parameters = [ch for ch in code[i][:-2]]
#             parameters.sort(reverse=True)
#             # print(f"{code[i]=}")
#             try:
#                 param_1 = parameters[0]
#             except IndexError:
#                 i += 1
#                 continue
#             try:
#                 param_2 = parameters[1]
#             except IndexError:
#                 param_2 = '0'
#             try:
#                 param_3 = parameters[2]
#             except IndexError:
#                 param_3 = '0'
            
#             if mode == '01':
#                 if param_1 == '0':
#                     one = int(code[int(code[i+1])])
#                 if param_1 == '1':
#                     one = int(code[i+1])
#                 if param_2 == '0':
#                     # print(f"{i+2=}")
#                     # print(f"{code[i+2]=}")
#                     two = int(code[int(code[i+2])])
#                 if param_2 == '1':
#                     two = int(code[i+2])
#                 if param_3 == '0':
#                     three = int(code[int(code[i+3])])
#                 if param_3 == '1':
#                     three = int(code[i+3])
#                 # print(f"{one=}")
#                 # print(f"{two=}")
#                 # print(f"{three=}")
#                 # # print(f"{code[two]}")
#                 # print(f"{i=}")
#                 # print(f"{code[i]=}")
#                 code[three] = str(one + two)

#             if mode == '02':
#                 if param_1 == '0':
#                     one = int(code[int(code[i+1])])
#                 if param_1 == '1':
#                     one = int(code[i+1])
#                 if param_2 == '0':
#                     two = int(code[int(code[i+2])])
#                 if param_2 == '1':
#                     two = int(code[i+2])
#                 if param_3 == '0':
#                     three = int(code[int(code[i+3])])
#                 if param_3 == '1':
#                     three = int(code[i+3])
#                 code[three] = str(one * two)
#             i += 4
#             continue
        
#         if code[i] not in ['1', '2', '3', '4', '99']:
#             i += 1
    

#         # if len(code[i]) > 1 and code[-2] + code[-1] == '01' or code[-2] + code[-1] == '02':
#         #     opcode = code[-2] + code[-1]
#         #     parameters = [ch for ch in code[:-2]]
#         #     parameters.sort(reverse=True)
#         #     if len(parameters) == 3:
#         #         code[int(code[i+3])] = str(int(code[i+1]) + int(code[int(code[i+2])]))
#         #     if len(parameters) == 4:
#         #         pass

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2019 Day 5 Advent of Code Input.txt"

# stream = open(file, 'rt')
# intcode = stream.read().strip().split(',')
# stream.close()

# parse_code(intcode)

#extract the code from the file and load it into an array for processing
input1 = open(file, "r")
code = input1.read()
input1.close()
code = code.split(",")
 
#the array elements are currently strings; turn them into integers
for i in range(len(code)):
    code[i] = int(code[i])
 
#function to return a five-element array to represent the intcode
def intcodeArray(int1):
    intcode = list(str(int1))
    if(len(intcode)<5):
        for i in range(5-len(intcode)):
            intcode.insert(0,"0")
    for i in range(len(intcode)):
        intcode[i] = int(intcode[i])
    return intcode
 
##inst[4] and inst[3] are the opcode
##inst[2] is the mode of the first parameter
##inst[1] is the mode of the second parameter
##inst[0] is the mode of the third parameter
 
#function to return the value of a position, given its mode
def value(mode, position):
    val = 0
    if(mode==0):
        val = code[code[position]]
    else:
        val = code[position]
    return val
 
pos = 0
 
#run the intcode
while(code[pos]!=99):
    
    inst = intcodeArray(code[pos])
 
    #add two values
    if(inst[4]==1):
        two = pos+1
        three = pos+2
        four = code[pos+3]
        
        code[four] = value(inst[2],two) + value(inst[1],three)
        pos += 4
 
    #multiply two values
    elif(inst[4]==2):     
        two = pos+1
        three = pos+2
        four = code[pos+3]
 
        code[four] = value(inst[2],two) * value(inst[1],three)
        pos += 4
 
    #take an input value
    elif(inst[4]==3):
        
        print("What is your input value?")
        choice = input()
        choice = int(choice)
        
        if(inst[2]==0):
            code[code[pos+1]] = choice
        else:
            code[pos+1] = choice
            
        pos += 2
 
    #print an output value
    elif(inst[4]==4):
        print(value(inst[2],(pos+1)))
        pos += 2
 
    #if first parameter != 0, jump to position given by the second parameter
    elif(inst[4]==5):
        
        two = pos+1
        three = pos+2
        
        if(value(inst[2],two)!=0):
            pos = value(inst[1],three)
        else:
            pos += 3
 
    #if first parameter is zero, jump to position given by the second parameter
    elif(inst[4]==6):
        
        two = pos+1
        three = pos+2
        
        if(value(inst[2],two)==0):
            pos = value(inst[1],three)
        else:
            pos += 3
 
    #based on whether first parameter < second parameter,
    #store 1 or 0 in the position given by the third parameter
    elif(inst[4]==7):
        
        two = pos+1
        three = pos+2
        four = code[pos+3]
        
        if(value(inst[2],two) < value(inst[1],three)):
            code[four] = 1
        else:
            code[four] = 0
        pos += 4
 
    #based on whether first parameter == second parameter,
    #store 1 or 1 in the position given by the third parameter.
    elif(inst[4]==8):
        
        two = pos+1
        three = pos+2
        four = code[pos+3]
        
        if(value(inst[2],two) == value(inst[1],three)):
            code[four] = 1
        else:
            code[four] = 0
        pos += 4