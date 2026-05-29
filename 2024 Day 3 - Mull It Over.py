import re # We're going to use regular expression tools to find sections of the string in the correct form.

def sumMuls(string):
    # Looks for strings in the form "mul([any num of digits],[same as before])". Places them into a list.
    lst = re.findall(r'mul\([-+]?\d+,[-+]?\d+\)' , string)

    # Take each list item, strip the "mul(" and ")" off the ends, split at the comma, turn each item into an
    # integer, and tuplify the result. Add the product of the two numbers to the cumulative sum.
    sum = 0
    for mul in lst:
        stripped_lst = tuple(map(int, mul.lstrip('mul(').rstrip(')').split(',')))
        sum += stripped_lst[0] * stripped_lst[1]
    
    return sum

def sumSomeMuls(string):
    m_do = re.search(r'do\(\)', string).start()
    m_dont = re.search(r"don't\(\)", string).start()
    m_mul = re.search(r'mul\([-+]?\d+,[-+]?\d+\)', string).start()

    if m_do < m_dont or m_mul < m_dont:
        sum = 0

        noDonts = string.split("don't()")
        do_end_list = [re.search(r"do\(\)", s).end() if "do()" in s else re.search(r"do\(\)", s) for s in noDonts]
        print(do_end_list)
        # sum_list = [sumMuls(s)]
        for i in range(len(noDonts)):
            if i == 0:
                sum += sumMuls(noDonts[i])
                print(sum)
                continue
            if "do()" in noDonts[i]:
                t = re.search(r'do\(\)', noDonts[i]).end()
                str_slice = noDonts[i][t:]
                sum += sumMuls(str_slice)
    return sum

i = 0
string = ''
while i < 6:
    string += input()
    i += 1
print(sumSomeMuls(string))



