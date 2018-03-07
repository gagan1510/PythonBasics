import sys
import time

f = None

try:
    f = open("poem.txt")

    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end = "")
        sys.stdout.flush()
        print("\nPress ctrl+c now!")
        time.sleep(2)

except IOError:
    print("Could not fine the file poem.txt")

except KeyboardInterrupt:
    print("You cancelled the reading from the file!")

finally:
    if f:
        f.close()
    print("The file has been closed!")