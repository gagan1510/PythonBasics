import sys

# print(sys.argv) # this prints the path of the current file

if len(sys.argv) > 2:
    print("Please supply a file name")
    raise SystemExit
f = open(sys.argv[0])  # this reads the command line argument!

svalues = f.readline()
for line in f:
    print(line)
print(svalues)
f.close()

# convert all str to float

fvalues = [float(s) for s in svalues]

# print("the maximum value is: ", max(fvalues))
# print("the minimum value is: ", min(fvalues))
