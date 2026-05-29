from hashlib import md5

input = "abbhdwsy"

def findPassword(s):
    i = 0
    password = ''
    while len(password) < 8:
        string = s + str(i)
        md5Str = md5(string.encode()).hexdigest()
        if all(md5Str[i] == '0' for i in range(5)):
            password += md5Str[5]
        i += 1
    return password

# Part 2

def findPassword2(s):
    passwordLst = ['' for i in range(8)]
    display = "_" * 8
    print(display)
    print("Decrypting...")
    i = 0
    while any(ch == '' for ch in passwordLst):
        string = s + str(i)
        md5Str = md5(string.encode()).hexdigest()
        if all(md5Str[i] == '0' for i in range(5)):
            if md5Str[5].isnumeric():
                if 0 <= int(md5Str[5]) < 8 and passwordLst[int(md5Str[5])] == '':
                    passwordLst[int(md5Str[5])] += md5Str[6]
                    display = ''
                    for ch in passwordLst:
                        if ch == '':
                            display += '_'
                        else:
                            display += ch
                    print(display)
                    if not all(ch.isalnum() for ch in display):
                        print("Decrypting...")
                    else:
                        print("Decryption complete.")
        i += 1

findPassword2(input)