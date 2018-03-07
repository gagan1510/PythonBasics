class A(object):
    x = 10
    def __init__(self, number):
        self.number = number

    # def __repr__(self):


    def meth1(self):
        print("Class A: Meth1()")

    def meth2(self):
        print("Class A: Meth2()")

class B(A):
    def meth3(self):
        print("Class B: Meth3()")

class C(B):
    def meth4(self):
        print("Class C: Meth4()")

class D(B):
    def meth5(self):
        print("Class D: Meth5()")

class E(object):
    def meth7(self):
        print("Class F: Meth7()")

class F(A, E):
    def meth6(self):
        print("Class E: Meth6()")

objC = C(5)
objC.__init__(7)
objC.meth1()
objC.meth2()
objC.meth3()
objC.meth4()
print(objC.number)
print(objC.x)


objD = D(5)
objD.meth5()
objD.meth1()
objD.meth2()
objD.meth3()
print(objD.number)

objF = F(4)
objF.meth2()
objF.meth1()
objF.meth6()
print(objF.number)