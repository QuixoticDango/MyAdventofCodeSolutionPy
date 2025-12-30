# 240298-784956
def is_valid(password):
    password = str(password)
    if not any(password[i] == password[i+1] for i in range(len(password) - 1)):
        return False
    if any(password[i] > password[i+1] for i in range(len(password) - 1)):
        return False
    return True

def is_valid_part2(password):
    if not is_valid(password):
        return False
    else:
        password = str(password)
        if any(password[i] == password[i+1] for i in range(len(password) - 2)):
            ch_dict = {ch:0 for ch in password}
            for ch1 in ch_dict.keys():
                ch_count = 0
                for ch2 in password:
                    if ch1 == ch2:
                        ch_count += 1
                ch_dict[ch1] = ch_count
            if not any(ch_dict[key] == 2 for key in ch_dict.keys()):
                return False
        return True
password_range = range(240298, 784956 + 1)

print(sum(1 for password in password_range if is_valid(password)))
print(sum(1 for password in password_range if is_valid_part2(password)))