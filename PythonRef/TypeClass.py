def printham(self):
    self.x = int(input("Enter number: "))
    print(self.x)

TypeClass = type("TypeClass", (object,), {"x" : 5, "printham" : printham})
t = TypeClass()
t.printham()

class SingleTon(type):
    _instances = {}
    def __call__(self, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingleTon, cls).__call__(*args, **kwargs)
            cls.x = 5
        return cls._instances[cls]

