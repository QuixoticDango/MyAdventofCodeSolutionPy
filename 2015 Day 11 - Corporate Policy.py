def newPassword(s):
    chList = [ord(c) - ord('a') for c in s]
    print(chList)
    straightCheck = False
    doublesCheck = False
    invalidLetterCheck = False
    checkList = [straightCheck, invalidLetterCheck, doublesCheck]
    while not all(checkList):
        chList[-1] = (chList[-1] + 1) % 26
        i = 0
        while i < len(chList):
            try:
                if chList[-1-i] == 0:
                    chList[-1-i-1] = (chList[-1-i-1] + 1) % 26
                else:
                    break
                i += 1
            except IndexError:
                i += 1
                pass
        if any(chList[i+2] - chList[i+1] == 1 and chList[i+1] - chList[i] == 1 
                   for i in range(len(chList) - 2)):
            checkList[0] = True
        else:
            checkList[0] = False
        if any(ch == 8 or ch == 11 or ch == 14 for ch in chList):
            checkList[1] = False
        else:
            checkList[1] = True
        if any(chList[i] == chList[i+1] and chList[j] == chList[j+1] and chList[i] != chList[j] 
               for i in range(len(chList) - 3)
               for j in range(i+2, len(chList) - 1)):
            checkList[2] = True
        else:
            checkList[2] = False
    password = ''.join([chr(n + ord('a')) for n in chList])
    return password


input = 'vzbxxyzz'
print(newPassword(input))