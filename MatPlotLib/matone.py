import matplotlib.pyplot as plt
import numpy

nyear = numpy.round(numpy.random.normal(2000 , 1000 , 60) , 1)
npop =  numpy.round(numpy.random.normal(2.5 , 1.0 , 60) , 1)
year = [1950 , 1970 , 1990 , 2010]
pop = [1.9 , 2.1 , 2.5 , 3.1]

plt.plot(year , pop) # used to plot the curve
plt.scatter(year, pop) # used to plot the points only

plt.xlabel("Year")
plt.ylabel("Population")
plt.yticks([0,1,2,3,4] , ['0','1B', '2B', '3B', '4B'])
plt.show()