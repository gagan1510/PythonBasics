def hello(name = 'gagan'):
    return 'hello ' + name

greet = hello

# now, greet has the value of hello
print(hello())
print(greet())

del hello
# but, even after deleting hellp, the greet function will work
print(greet)

print(greet())

# greet wasn't attached to hello!