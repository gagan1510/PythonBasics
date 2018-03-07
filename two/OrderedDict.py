# a normal dictionary doesn't retain the order coz it's just a mapping!

from collections import OrderedDict

d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k, v in d.items():
    print(k, v)

#the ordered dictionary's sequence will be kept

print("The following is an ordered dictionary: ")

dord = OrderedDict()

dord['a'] = 1
dord['b'] = 2
dord['c'] = 3
dord['d'] = 4
dord['e'] = 5

for k, v in dord.items():
    print(k,v)

# same keys and values of to normal dictionary make them the same
# but in ordered dict, if the keys and values of the dict are not in the same sequence then they'll not be the same

