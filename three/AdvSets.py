s = set()

s.add(1)
s.add(2)
s.add(3)
print(s)

sc = s.copy()

sc.add(10)

print(sc.difference(s))

a = {1,2,3,4,5}
b = {1,2,7,8,9}

a.difference_update(b) #this set removes the common elements of a and b from a

print(a)

a2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b2 = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

print(a2.intersection(b2)) # this will print the common elements of a2 and b2
# and intersection_update is same as the difference_update

# the is disjoint function returns true or false on the basis of if they have an intersection or not