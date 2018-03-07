from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age = 2, breed ='lab', name='sammy')

print(sam)

# sam has all the attributes of a class
# and the members will behave as the data members