def countTokens(array):
    clawTokens = []
    for claw in array:
        # These formulas come from solving the algebra problem by substitution. Solving part 2 only requires that you
        # add whatever number (in my case 10000000000000) to the "Prize" values (i.e. the solutions to your two equations)
        num_a = (claw[2] * (claw[5] + 10000000000000) - (claw[4] + 10000000000000) * claw[3]) / (claw[2] * claw[1] - claw[0] * claw[3])
        num_b = ((claw[4] + 10000000000000)  - claw[0] * num_a) / claw[2]
        tokens = num_a * 3 + num_b
        clawTokens.append(num_a * 3 + num_b)

    sum = 0
    for tokens in clawTokens:
        # Converting a float value to int cuts off the decimal value without rounding. If the float value is already
        # an integer (0 after decimal point), then this difference will be 0.
        if tokens - int(tokens) == 0:
            sum += tokens
    return sum

# File path simply gives the location of my input, which I have copied into a Notepad text file.
file_path = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2024 Day 13 Advent of Code Input.txt"
with open(file_path, 'r') as f:     # Open the file with alias "f". Execute the following code. Close the stream.
    clawArray = [[]] # Creates a nested list. I want each claw to be in it's own list inside the total list of claws.
    rawText = [line.strip().split(',') for line in f.readlines()] # Strip whitespace and split at the comma.
    clawCount = 0   # I'll use this as an index for each claw.
    for line in rawText:
        x = ''      # x and y are set to empty strings every time a new line is reached
        y = ''   
        # Finds numbers in strings. Adds them to x if we're looking at the 0th value and y if we're at the 1st.   
        for i in range(len(line)): 
            for ch in line[i]:
                if ch.isnumeric() and i % 2 == 0: 
                    x += ch
                if ch.isnumeric() and i % 2 != 0:
                    y += ch
            # If we reach an empty string, that means we're going to a new claw. Add 1 to the clawCount index
            # and append a new list into which the new claw will be stored. Use continue to skip the final steps.
            if line[i] == '':
                clawCount += 1
                clawArray.append([])
                continue
            elif i % 2 == 0:
                clawArray[clawCount].append(int(x))
            else:    
                clawArray[clawCount].append(int(y))

print(countTokens(clawArray))