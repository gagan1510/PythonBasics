import random

def gensquares(n):
    for i in range(n):
        yield i**2

for sq in gensquares(5):
    print(sq)

print("\n")

def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for ran in rand_num(1, 10, 6):
    print(ran)