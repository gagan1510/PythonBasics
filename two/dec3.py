def hello():
    return 'Hello Gagan!'

def other(func):
    print("The argument function has been called!")
    print(func())
    return

other(hello)

# here, we've passed hello to the other function

