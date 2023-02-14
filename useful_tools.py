import re
import sys

import pyperclip as pyperclip

# clipboard operation
pyperclip.copy('aaaa')
text = pyperclip.paste()  # you can paste now
print(text)

# args
# argslen = len(sys.argv)
# if argslen < 2:
#     print('usage: python3 useful_tools.py [any string word] - echo')
#     sys.exit()
# word = sys.argv[1]
# print(word)


# regex
zh_mobile_reg = re.compile(r'\d{11}')  # china phone number
mo1 = zh_mobile_reg.search('12345678910')
mo2 = zh_mobile_reg.search('12345678dddd910')
print(mo1.group())
print(mo2)
# regex group
zh_mobile_reg = re.compile(r'(\d[86])(\d{11})')  # china phone number
mo = zh_mobile_reg.search('8612345678910')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.groups())  # ('86', '12345678910')
# regex match first
match_first = re.compile(r'(a|b)')
mo = match_first.search('my name is bob')
print(mo.group())  # a
# greedy match
greedy_reg = re.compile(r'(ab){3,5}')  # match 5 times
mo1 = greedy_reg.search('ababababababcd')
print(mo1.group())
un_greedy_reg = re.compile(r'(ab){3,5}?')  # match 3 times
mo2 = un_greedy_reg.search('ababababababcd')
print(mo2.group())
