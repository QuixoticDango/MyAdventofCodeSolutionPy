input = '1113122113'


count = 0
while count < 50:
    digitCount = []
    digitIndex = 0
    for i, ch in enumerate(input):
        if i == 0:    
            digitCount.append([1, ch])
        elif ch == input[i-1]:
            digitCount[digitIndex][0] += 1
        else:
            digitCount.append([1, ch])
            digitIndex += 1
    input = ''.join([str(n1) + n2 for n1, n2 in digitCount])
    count += 1
print(len(input))