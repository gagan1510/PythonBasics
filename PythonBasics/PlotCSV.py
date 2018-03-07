from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x,y = np.loadtxt('sample1.csv', unpack=True, delimiter=',')

plt.title('Epic Chart')

# print(x)
# print(y)

plt.plot(x,y)

plt.show()