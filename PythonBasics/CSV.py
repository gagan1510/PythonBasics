import csv

with open('sample.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')

    colors = []
    dates = []

    for row in readCSV:
        color = row[3]
        date = row[0]

        colors.append(color)
        dates.append(date)

print(dates)
print(colors)

whatColor = input("What color do you want to know the date of?")
coldex = colors.index(whatColor)
print("The date of the color you entered is: ", dates[coldex])
