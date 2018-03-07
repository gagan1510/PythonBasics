import re

f = open('test.txt')
for line in f:
    line = line.rstrip()
    if line.find("This") >= 0:
        print(line)
    else:
        print("This is not a test file")

f.close()

print("\n")

# this is checking that if the line in the file starts with the 'This'
# also, the lines not starting with a 'This' are not being printed

s1 = "This is a string"
print(s1.rstrip("string"))

# this will be removed from the string

print("\n")

f = open('test.txt')

for line in f:
    line = line.rstrip()
    if re.search('this', line):
        print(line)
f.close()
#this loop prints all the lines that contain 'this' word in it

print()

f = open('test.txt')

for line in f:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)

f.close()

print()

f = open('test.txt')

for line in f:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line)

f.close()

# this ^ sign shows that the From: should be at the starting of the line

# ^ <-- start of the line
# . <-- any character
# * <-- any number of characters

print()

s1 = 'This is a 19 string having 34 some 56 numbers in it 90'
lNo = re.findall('[0-9]+', s1)
print(lNo)   # finds all the numbers of the string and stores it in lNo list as STRINGS

print()