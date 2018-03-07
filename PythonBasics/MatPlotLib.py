from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')


x = [5,6,7,8]
y = [7,3,8,3]


x1 = [5,6,7,8]
y1 = [6,7,2,6]

x2 = [1,3,5,7]
y2 = [1,4,8,10]


x3 = [2,4,6,8]
y3 = [4,6,7,9]

plt.bar(x2, y2, color = 'g', align = 'center')
plt.bar(x3, y3, color = 'c', align = 'center')
# plt.plot(x1, y1, color = 'g', linewidth = 5, label = 'line 2')
# plt.scatter(x, y, color = 'k')

plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

# plt.legend()


plt.show()