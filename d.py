# import re
# string = 'abc'
# s = re.search(r'[a-z][a-z][a-z]', string)
# print(string[s.start():s.end()])
# print(0b0)
# print(0b0 | 0b1)
# print(0b0 & 0b1)
# print(0b0 ^ 0b1)

# string = '123 -> x'
# print(string.split(' -> '))
# print(sum(ch for i, ch in list(enumerate(bin(0xffff)))))
# print(max([0, 1, 3, 4, 4, 5]))
# s = 'sdlfkj lkjdfl skj'
# t = s.find(' ')
# print(t)

# print('a' < 'b')
# lst = [['a', 1], ['b',2],['c',3], ['d',4]]

# lst = lst[:1] + lst[2:3] + lst[1:2] + lst[3:]
# print(lst)

# print(divmod(20,8)[0], divmod(20,8)[1])

# string = 'stars stat start'

# print(string.find('stat'))

# import re

# s = "2wysextplwqpvipxdv[srzvtwbfzqtspxnethm]syqbzgtboxxzpwr(kljvjjkjyojzrstfgrw)obdhcczonzvbfby[svotajtpttohxsh]cooktbyumlpxostt"
# s2 = 'abdegoapfabc;akj  def adfoa abcdefdef'
# p =              r'\[([^\]]+)\]'
# print(re.findall(r"\[([a-z]+)\]", s))

# import re 
 
# Example string 
# text = "John 123-45-6789 Jane 987-65-4321" 
 
# # Regex pattern with capturing groups 
# pattern = r"(\d{3})-(\d{2})-(\d{4})" 
 
# # Finding all matches 
# matches = re.findall(pattern, text) 
 
# # Output the captured groups 
# # for match in matches: 
# #     print("Captured groups:", match) 

# # print(matches)
# import re
# s = 'abcdefg'
# t = 'bcdefg'
# u = 'cdefg'
# v = 'defg'
# print(list(zip(s, t, u, v)))
# print(re.search('h',s))

lst = [(3, 5), (10, 14), (12, 18), (16, 20), (3, 18), (4,6)]
lst.sort(key=lambda s: (s[0], -s[1]))
print(lst)