def kwargTester(**kwargs):
    for i in kwargs:
        print(i, kwargs[i])
    return

kwargTester(s = 'gagan')