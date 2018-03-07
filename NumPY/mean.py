import numpy

height = numpy.round(numpy.random.normal(1.75 , 0.20 , 5000) , 2) # np.rndm.nrml(pt, deviation, amount)
weight = numpy.round(numpy.random.normal(60.32 , 15, 5000) , 2)

np_city = numpy.column_stack((height,weight)) # this stores height and weight in the form of list of list
print(np_city)