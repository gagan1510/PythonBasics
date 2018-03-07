import matplotlib.pyplot as plt
import numpy

x = numpy.random.normal(10,10,10)

y = numpy.random.normal(10,10,10)

z = numpy.random.normal(1000,100,10)

np_x = numpy.array(x)
np_y = numpy.array(y)
np_z = numpy.array(z)
np_z *= 2

# print(x)
# plt.hist(x , bins = 10)
# plt.hist(y, bins = 10)

plt.scatter(np_x, np_y, s = np_z , c = 'red' , alpha=0.8)
plt.text(2 , 3 , 'India')
plt.grid(True)

plt.show()