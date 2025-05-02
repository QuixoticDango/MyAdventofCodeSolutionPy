import re

def isValid(row):
    # Get the range of valid inputs and put into tuple because it won't need to be updated
    valid_range = tuple(map(int, row[0].split('-')))
    # Get the letter that needs to be checked and remove the colon at the end.
    check_letter = row[1][0]
    # Get password
    password = row[2]
    # Count instances of the letter using findall from regular expressions module. This could also be done
    # with a for-loop.
    instances = len(re.findall(check_letter, password))

    if valid_range[0] <= instances <= valid_range[1]:
        return True
    else:
        return False

def isValid2(row):
    # Get the indices of valid inputs and put into tuple because it won't need to be updated
    valid_index = tuple(map(lambda x: int(x) - 1, row[0].split('-')))
    # Get the letter that needs to be checked and remove the colon at the end.
    check_letter = row[1][0]
    # Get password
    password = row[2]

    # No need to check further if the letter isn't present in the password.
    if check_letter not in password:
        return False
    
    # Scan the password and check in the letter is in the valid positions.
    password_index = []
    for i in range(len(password)):
        if password[i] == check_letter and i == valid_index[0]:
            password_index.append(i)
        if password[i] == check_letter and i == valid_index[1]:
            password_index.append(i)

    # If the letter is in both or neither position, the password is invalid.
    if len(password_index) != 1:
        return False
    print("Valid.")
    return True

valid_rows = 0
while True:
    row = input().strip().split()

    if row == []:
        break

    if isValid2(row):
        valid_rows += 1

print(f"The number of valid passwords is {valid_rows}")
