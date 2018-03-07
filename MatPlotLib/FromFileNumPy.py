import matplotlib.pyplot as plt
import numpy as np

x,y = np.loadtxt("example.csv", delimiter=",", unpack = True)

plt.plot(x, y, color = 'c', label = "CSV Graph")

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()

plt.show()