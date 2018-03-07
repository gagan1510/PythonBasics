
# here, we have defined a function inside a function

def hello(name = 'gagan'):

    def greet():
        return '\t The greet() is being called!'

    def welcome():
        return '\t The welcome() is being called'

    if name == 'gagan':
        return greet
    else:
        return welcome

x = hello()

print(x)

print(x())

# here, the function hello is not returning the value of greet but the function itself
# and the x is being changed to a function being assigned


# NOTE: The scope of welcome and greet is only inside the hello function