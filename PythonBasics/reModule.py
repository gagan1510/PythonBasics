'''
IDENTIFIERS

\d any number
\D anything but a number
\s a space
\S anything but a space
\w a character
.  any character except a new line
\b the white space around words
\. a period

MODIFIERS

{1, 3} we're expecting 1 to 3 of it
+ match one or more
? match 0 or 1
* match 0 or more
$ the end of a string
^ the beginning of a string
| either or
[] range or "variance" [A-Za-z]
(x) expecting x amount

WHITE SPACE CHARACTER

\n new line
\s space
\e escape
\f form feed
\r return

DON'T FORGET

. + * ? [ ] $ ^ ( ) { } | \

'''

import re

exampleString = '''
Jessica is 16 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar is 102.
'''

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

print(ages)
print(names)