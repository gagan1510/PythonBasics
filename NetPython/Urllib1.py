# using urllib, we can handle a web page just like a file!
# this is a shorter and simpler version of Socket module

import  urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())