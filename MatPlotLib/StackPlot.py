import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,5]
working = [7,8,7,2,7]
playing = [8,5,7,8,5]

plt.plot([],[], linewidth = 2, color = 'm', label = 'sleeping')
plt.plot([],[], linewidth = 2, color = 'c', label = 'eating')
plt.plot([],[], linewidth = 2, color = 'r', label = 'working')
plt.plot([],[], linewidth = 2, color = 'k', label = 'playing')

plt.stackplot(days, sleeping,eating,working,playing, colors = ['m', 'c', 'r', 'k'])

plt.xlabel("Days")
plt.ylabel("Task")
plt.legend()

plt.show()