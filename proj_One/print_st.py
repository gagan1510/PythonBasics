age = 18
name = "gagan singh"

print("my name is {0} and my age is {1}".format(age, name))

print("{:.3f}".format(1.0/3)) # in {}, the :.3f is the number of digits to be printed after the decimal

print("{:$^11}".format("gagan")) # the {:_^} increases the length of the string by adding _ before and after it

print("gagan", end="")
print("preet", end=" ") # the end="" will replace "\n" after end of every print statement and in " ", we write the last char to be printed
print("singh")

print('What\'s your name?') # \ is the escape sequence so that the compiler doesn't get confused b/w end of string and the ' to be printed
print("This is the first sentence. \
      This is the second sentence")

print(r"\'This is a new line") # r is used to keep the string unprocessed