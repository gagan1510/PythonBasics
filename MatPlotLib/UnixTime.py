import datetime as dt
import time

example = time.time()

print("The UNIX time is: ")
print(example)

print("The real time is: ")
print(dt.datetime.fromtimestamp(example))