import copy

a = [1,2,3,4,5,6,7,8]
b = a # the reference of a has been created!
c = copy.deepcopy(a) # this creates a  new object and copies all the objects

b[2] = -10 # this changes the value in a too!

print(a)
print(c)

del a

p = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(p[::3]) # prints every 3rd object from the beginning

st = ['hello', 'gagan', 'preet', 'singh']
# x[a:b:c] copies every cth object starting from a to b
# in the same way, we can delete the elements too from the list
print(p.__getitem__(4)) # returns the item at index 4

_iter = st.__iter__()
while 1:
    try:
        x = _iter.__next__()
        print(x)
    except StopIteration:
        break

print()
wel = 'Hello %s %s'
print(wel)
wel = wel % ('Gagan', 'Singh')
print(wel)
