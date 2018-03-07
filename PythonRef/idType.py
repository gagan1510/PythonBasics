import types

x = 10
y = [1, 2, 3, 4, 5, 6, 7]
z = 20

print("The id of x is: " + str(id(x)))

if x is y:
    print("both are the same.")
else:
    print("both variables are different.")

if type(x)is list:
    print("x is list")
elif type(x) is int:
    print("x is integer")
elif type(x) is float:
    print("x is float")

m = None
if m is None:
    print("m is none")
else:
    print("m is int")