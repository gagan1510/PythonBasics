# this function accepts a line until enter is pressed!

import sys

text = ""
def gets():
    global text
    while 1:
        c = sys.stdin.read(1)
        if c == '\n': break
        text = text + c
    return text

full = gets()
print(full , end=".")