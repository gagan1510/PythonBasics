import numpy

x= [1,2,3,4,5,6,7]
y = [10, 11, 12, 13, 14, 15, 16]

npx = numpy.array(x)
npy = numpy.array(y)

b = npy/npx
npb = numpy.array(b)
print(list(b))
