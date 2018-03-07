import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()

def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)
        xs.append(x)
        ys.append(y)

    return xs,ys


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=2, colspan=1) # 6 y divisions, and the whole of x is taken
# rowspan = 2 says that 2 y divisions are being taken at once
# colspan = 1 says that 1 x division(remains undevided) is taken at once
# Starts from (0,0)
ax2 = plt.subplot2grid((6,1), (2,0), rowspan=2, colspan=1) # since rowspan = 2 therefore the 2nd one will start from 2
ax3 = plt.subplot2grid((6,1), (4,0), rowspan=2, colspan=1)

# # add_subplot syntax
#
# ax1 = fig.add_subplot(2,2,1) # 2x2x1
# ax3 = fig.add_subplot(2,2,2) # 2x2x2
# ax2 = fig.add_subplot(2,1,2) # 2x1x2

x , y = create_plots()
ax1.plot(x,y, color = 'b')

x , y = create_plots()
ax2.plot(x, y, color = 'g')

x , y = create_plots()
ax3.plot(x, y, color = 'g')

plt.show()