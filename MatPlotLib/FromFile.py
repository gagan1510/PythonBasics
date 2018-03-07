import csv
import matplotlib.pyplot as plt

x = []
y = []

with open('example.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, color = 'c', label = "CSV Graph")

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()

plt.show()