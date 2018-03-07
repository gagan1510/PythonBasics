class Complex:
    def __init__(self, imag, real):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return "Complex(%s, %s)" % (self.real, self.imag)

    def __str__(self):
        return "(%g + %gj)" % (self.real, self.imag)

    def __add__(self, other):
        return Complex(self.real + other.real , self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real , self.imag - other.imag)

    def __radd__(self, other):
        return Complex.__add__(other, self)

    def __rsub__(self, other):
        return Complex.__sub__(other, self)


a = Complex(4, 6)
print(" ", a)

b = Complex(6, 4)
print("+", b)

print(" ------------")
c = a + b
print(" ", c)

print(isinstance(a, Complex)) # this returns true when the first argument is of the type '2nd argument' n