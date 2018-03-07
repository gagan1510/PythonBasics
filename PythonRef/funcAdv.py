import  functools

def foo(x):
    x[3] = -55


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("a before foo(): ")
print(a)
foo(a)

print("a after foo(): ")
print(a)

def fabonacci(f):
    def compute(x):
        return x
    return compute

m = fabonacci(foo) # m has been assigned the value of compute() as the function returns
print(m(10))

# LAMBDA is used to define functions
print("Example of 'lambda' function: ")
a = lambda x,y : x+y
print(a(10, 20))

b = [1, 2, 3, 4, 5, 6, 7, 8]
tuck = lambda a : a**2
li = map(tuck, b)

print("The following is the list generated by the map(tuck, b): ")
for i in li:
    print(i)

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [10, 11, 12, 13, 14, 15]
z1 = zip(l1, l2 ) # this creates a list of tuples having [(l1, l2), (l1, l2), (l1, l2), (l1, l2)]

sum = lambda a, b: a+b
to_sum = range(1, 11)
all_sum = functools.reduce(sum, to_sum)
print('The sum of all the numbers of range is: ')
print(all_sum)

print("The filtered numbers are:")
c = filter(lambda x: x<4, to_sum)
for i in c:
    print(i,)