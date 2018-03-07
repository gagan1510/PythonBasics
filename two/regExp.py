import re

lis = ['text1', 'text2', 'text3']
text = 'this is a string containing text1 but not the other texts'

for word in lis:
    if re.search(word, text):
        print()
        print('The word {} is there'.format(word))
    else:
        print()
        print("The word {} is not there!".format(word))

match = re.search(lis[0], text)

print()
#print(match)

print(match.start())
print(match.end())

print(text[28:34])
txt2 = "this is a text which has an @ in it, it is also used for decorators!"

#this splits the list into parts that are before and after the @ character
lis2 = re.split('@', txt2)
print(lis2)

txt = "This is a string which has many string words in a single string!"
x = re.findall('string', txt)
print(x) #this will print all the string words in the txt string

# to find a character from a group of characters

txt2 = 'this is a ! character @ having a lot of * unnecessary . punctuation ) marks'

lis_txt2 = re.split(" ", txt2)

li2 = re.findall('[!.@*)]+', txt2)
# the plus sign is for one or more occurences
print(li2)
