def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10):
    print(x)

# The generators are used to resume a loop from where it left
# Also, the yeild function doesn't keep a track of the answers or results
# Instead, it returns the value for each number and executes again for the next one

def genfib(x):
    a = 1
    b = 1
    for i in range(x):
        yield a
        temp = a
        a = b
        b = temp + b

for i in genfib(8):
    print(i, end= "   ")

# we can get the next to be yielded value by using the next function

print("\n")

def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()
print(next(g))
print(next(g))
print(next(g))
#print(next(g)) the g function will not work here since the number is goig out of the range

# To convert a string from iterable to iterator

print()
print()

s = 'hello'
s_iter = iter(s)

print(list(s_iter))

#print(next(s_iter))

