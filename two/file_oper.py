f = open('test.txt')
print(f.read())
print(f.read()) # the cursor will be at the end of the file after using read() once

f.seek(0) # this will send the cursor back to the beginning of the file

print(f.read())

f.seek(0)

x = f.readlines() #this will store all the lines of the file as the elements of the string

print(x)
