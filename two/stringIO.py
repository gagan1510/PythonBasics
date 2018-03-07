import io

message = 'This is a string on which we will apply the file funtions'
f = io.StringIO(message)
print(f.read())

#the StringIO is used to create a file in which the string is to be stored
