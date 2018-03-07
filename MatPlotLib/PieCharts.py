import matplotlib.pyplot as plt


days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,5]
working = [7,8,7,2,7]
playing = [8,5,7,8,5]

slices = [7,2,2,13]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['m', 'c', 'r', 'b']

plt.pie(slices, labels = activities,
        colors = colors, startangle=90,
        shadow=True, explode=(0,0.05,0.05,0.05 ),
        autopct = '%1.1f%%')

plt.show()

# the explode moves the slices outwards in the same order of the list