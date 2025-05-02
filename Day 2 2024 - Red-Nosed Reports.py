import statistics as stat

def isSafe(rows):
    if len(rows) < 2:
        return False
    if len(rows) == 2 and (1 <= abs(rows[1] - rows[0] <= 3)):
        return True
    if rows[1] - rows[0] > 0:
        isDesc = False
    if rows[1] - rows[0] < 0:
        isDesc = True

    for i in range(len(rows) - 1):
        difference = rows[i + 1] - rows[i]
        if difference == 0:
            return False
        if abs(difference) > 3 or abs(difference) < 1:
            return False
        if isDesc and difference > 0:
            return False
        if not isDesc and difference < 0:
            return False
    return True

def Dampener(rows):
    # Check for duplicates first. Count and delete them.
    dupes = 0
    for i in range(len(rows) - 1 - dupes):
        d = rows[i+1 - dupes] - rows[i - dupes]
        if d == 0:
            del rows[i - dupes]
            dupes += 1
    
    # If you have more than two duplicates, no further testing is needed.
    if dupes > 1:
        print(f"{dupes} duplicates found.")
        print('UNSAFE: TOO MANY DUPES.')
        return False
    
    # Only rows w/ 0 or 1 duplicates are left. Use your function/method from part 1
    # to check if the row is safe.
    if isSafe(rows):
        print('SAFE: RAN isSafe() AFTER DUPE CHECK')
        return True

    # If your row isn't safe and a duplicate was deleted, that means you'd need to 
    # change at least 1 more thing. It's unsafe.
    if dupes == 1:
        print('UNSAFE: NOT SAFE AFTER DELETING ONE DUPE')
        return False
    
    # Only lists with no duplicates make it here.
    # The only problems left are have too large of a difference,
    # or switching direction.

    # If the sorted list matches the original list, the list is ascending.
    # If it's ascending and there's a dif greater than 3, it can't be corrected
    # unless deleting the 1st or last number fixes it. This applies to a
    # descending list as well.
    if sorted(rows) == rows:
        for i in range(len(rows) - 1):
            if abs(rows[i+1] - rows[i]) > 3:
                a_rows = rows[:]
                del a_rows[-1]
                b_rows = rows[:]
                del b_rows[0]
                if isSafe(a_rows):
                    print('SAFE: ASC LIST WHERE LAST VALUE WAS TOO LARGE')
                    return True
                elif isSafe(b_rows):
                    print('SAFE: ASC LIST WHERE FIRST VALUE WAS TOO SMALL')
                    return True
                else:
                    print('UNSAFE: ASC LIST WHERE NOT LAST/FIRST VALUE WAS TOO LARGE/SMALL')
                    return False
    
    # See above.
    if sorted(rows, reverse=True) == rows:
        for i in range(len(rows) - 1):
            if abs(rows[i+1] - rows[i]) > 3:
                c_rows = rows[:]
                del c_rows[0]
                d_rows = rows[:]
                del d_rows[-1]
                if isSafe(c_rows):
                    print('SAFE: DESC LIST WHERE FIRST VALUE WAS TOO LARGE')
                    return True
                elif isSafe(d_rows):
                    print('SAFE: DESC LIST WHERE LAST VALUE WAS TOO SMALL')
                    return True
                else:
                    print('UNSAFE: DESC LIST WHERE NOT FIRST/LAST VALUE WAS TOO LARGE/SMALL')
                    return False
    
    # Only lists that are neither asc or desc with 0 dupes make it here.

    # If you have too large of a difference, make two new lists: one where
    # you delete the num at index 'i' and another where you delete at 
    # index 'i+1'. Use function from part 1 to check if either one is now safe.
    # If not, it's unfixable.
    # If there are no differences that are too big, you build a list of the differences.
    diff_list = []
    for i in range(len(rows) - 1):
        difference = rows[i+1] - rows[i]
        if abs(difference) > 3:
            e_rows = rows[:]
            del e_rows[i]
            f_rows = rows[:]
            del f_rows[i+1]
            if isSafe(e_rows):
                print('SAFE: "NEITHER" LIST WITH TOO LARGE NUM DELETED')
                return True
            elif isSafe(f_rows):
                print('SAFE: "NEITHER" LIST WITH TOO LARGE NUM DELETED')
                return True
            else:
                print('UNSAFE: "NEITHER" LIST STILL UNSAFE AFTER DEL LARGE NUM')
                return False
        diff_list.append(difference)

    # Count the neg and pos differences in diff_list.
    neg = 0
    pos = 0
    for dif in diff_list:
        if dif < 0:
            neg += 1
        else:
            pos += 1
    
    # If you have more than one of each, your list moved at least twice in both directions.
    # This is unfixable in one step.
    if neg > 1 and pos > 1:
        print('UNSAFE: LIST SWITCHES DIR AT LEAST TWICE')
        return False
    
    # If you have a single negative or positive difference, make two new lists and delete both
    # of the potential culprits like before. Chwck if they're safe.
    if neg == 1:
        neg_index = diff_list.index(min(diff_list))
        g_rows = rows[:]
        del g_rows[neg_index]
        h_rows = rows[:]
        del h_rows[neg_index + 1]
        if isSafe(g_rows):
            print('SAFE: NEG DIF CAUSE REMOVED')
            return True
        elif isSafe(h_rows):
            print('SAFE: NEG DIF CAUSE REMOVED')
            return True
        else:
            print('UNSAFE: NEG DIF REMOVED, STILL UNSAFE')
            return False
    
    if pos == 1:
        pos_index = diff_list.index(max(diff_list))
        i_rows = rows[:]
        del i_rows[pos_index]
        j_rows = rows[:]
        del j_rows[pos_index + 1]
        if isSafe(i_rows):
            print('SAFE: POS DIF CAUSE REMOVED')
            return True
        elif isSafe(j_rows):
            print('SAFE: POS DIF CAUSE REMOVED')
            return True
        else:
            print('UNSAFE: POS DIF REMOVED, STILL UNSAFE')
            return False
        

safe_rows = 0
row = [0]
while True:
    row = list(map(int, input().split()))
    if not row:
        break
    if Dampener(row):
        safe_rows += 1
print(safe_rows)