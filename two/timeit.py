import timeit

y = timeit('"-".join(str(n) for n in range(100))', number = 10000)

print(y)