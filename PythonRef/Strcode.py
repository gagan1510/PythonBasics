class A(object):
    def foo(self, x):
        print("Executing foo(%s, %s)"%(self,x))

    @classmethod
    def class_foo(cls, x):
        print("Executing class_foo(%s, %s)"%(cls, x))

    @staticmethod
    def static_foo(x):
        print("Executing static_foo(%s)"%(x))

obj = A()
obj.foo('gagan') # object is implicitly passed
obj.class_foo('gagan') # the object instance is implicitly passed
obj.static_foo('gagan') #  neither self nor cls is implicitly passed but a class instance is required to call