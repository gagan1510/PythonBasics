class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)

s = Stack()
s.push(3)
s.push('gagan')
s.push(5)
s.push(2)
s.push([8, 4, 5, 6])
x = s.pop()
y = s.pop()
print(x, y)
# print(id(x))
del s