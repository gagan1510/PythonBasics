def lessthan(n):
    i = 0
    while i<n:
        yield i
        i += 1
    return

print("The numbers less than 6 are being generated.")
for i in lessthan(6):
    print(i)

