from collections import defaultdict

d = {'k1' : 1}

# if we try to access keys which are not present in the dict,
# the compiler will throw an error message

#the defaultdict will never throw a key error and will create a key and assign the arg value to it

d2 = defaultdict(object)

x = d2['one']

print(x)

print()

for i in d2:
    print(i, ":", d2[i])

print()

d3 = defaultdict(lambda: 0)

print(d3['one'])

print()

d3['two'] = 4

print(d3)

# if there's no assignment for the key, the defaultdict will assign 0 to it

