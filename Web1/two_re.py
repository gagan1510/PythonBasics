import re

f = open('test2.txt')
l_no = list()

for line in f:
    stuff = re.findall('^This.+: ([0-9.]+)', line)
    if len(stuff)!=1: continue
    num = float(stuff[0])
    l_no.append(num)

# print(l_no)
print('Maximum', max(l_no))