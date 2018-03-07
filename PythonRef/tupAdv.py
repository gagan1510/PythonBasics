# TUPLES

a = (1, 2, 3, 4, 5, 6, 7)
b = (7, 8, 9, 10, 11, 12)

ab = (a, b)

# all these are tuples
print(a)
print(b)
print(ab)

print("\nSets begin here:")

# SETS
s = {1, 2, 3, 4} #  or this can be written as set([1, 2, 3, 4])
t = set('hello')

print(s)
print(t) # in a set, an element can occur only once! like, only one 'l' in this case

x = {1, 2, 3, 4, 5, 6, 7}
y = {8, 9, 10 , 11}

union = x | y
intersection = x & y
difference = x - y
symmetric = x ^ y # items uncommon

# adding element to the set
x.add(11)
y.update([3, 2, 1])
t.add('x')
print(x, y, t)

s.remove(1) # removing the element from the set
print(s)