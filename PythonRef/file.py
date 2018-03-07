fName = input("Please enter the file name with extension to be read: ")

try:
    f = open(fName)
    line = f.readline()

    while line:
        print(line, )
        line = f.readline()

    f.close()

    print("This is being printed using the for loop.\n")

    for line in open(fName):
        print(line)
    f.close()

    year = 20
    principle = 2000
    f = open(fName, "w")
    f.write("%3d    %.2f\n" % (year, principle))

    f.close()
except Exception:
    print("Couldn't find file " + fName)