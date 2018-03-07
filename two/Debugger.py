import pdb
#this module is used to manually debug the program

x = [1,2,3,4,5]
y = 6
z = 10

print(y + z)

pdb.set_trace()  # set_trace() pauses the program for a while and
                 # takes the variable and operations and shows their value and result of the operation
print(x + z)

