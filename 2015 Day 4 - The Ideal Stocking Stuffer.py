import hashlib

i = 1000000
while i <= 9999999:
    string = '0' * (7 - len(str(i))) + str(i)
    code = 'yzbqklnj' + string
    bytesCode = code.encode()
    md5Hash = hashlib.md5(bytesCode)
    finStr = md5Hash.hexdigest()
    if all(finStr[i] == "0" for i in range(6)):
        break
    i += 1
print(finStr)
print(i)