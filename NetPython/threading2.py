import threading
import  time

def timer(name, delay, repeat):
    print("Timer: " + name + " Started")
    while repeat>0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print("Timer: " + name + " completed")

def Main():
    t1 = threading.Thread(target = timer, args = ("Timer1", 0.0, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 0.0, 5))
    t1.start()
    t2.start()
    print("Main completed!")

if __name__ == '__main__':
    Main()