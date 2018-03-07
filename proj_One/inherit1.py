class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialised school member {}'.format(self.name))

    def tell(self):
        print("Name: {}  Age: {}".format(self.name, self.age), end=' ')


class teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        print('Initialized teacher: {}'.format(self.name))
        SchoolMember.tell(self)
        print('Salary: {}'.format(self.salary))


class student(SchoolMember):
    def __init__(self, name , age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

    def tell(self):
        print('Initialized student: {}'.format(self.name))
        SchoolMember.tell(self)
        print('Marks: {:.2f}'.format(self.marks))


t = teacher('Prof. Samir Jain', 30, 30000)
print()
s = student('Gaganpreet Singh', 18, 8.62)

t.tell()
print()
s.tell()