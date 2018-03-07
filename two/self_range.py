def self_range(x , y):
    while x != y:
        yield x
        x += 1


for i in self_range(0, 5):
    print(i)