x = int(input())
while x > 0:
    n = int(input())
    y = []
    count = 0
    for i in range(0, n):
        p = int(input())
        y.append(p)
    m = min(y)
    for i in range(0, n):
        if i == m:
            count += 1
    if count%2 == 0:
        print("Lucky")
    else:
        print("Unlucky")
    x = x - 1