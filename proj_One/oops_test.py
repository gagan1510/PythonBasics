class robot:
    pop = 0

    def __init__(self, name):
        self.name = name
        print("Initializing {}".format(self.name))

        robot.pop += 1

    def die(self):
        print("{} has been destroyed".format(self.name))
        robot.pop -= 1

        if robot.pop == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots left".format(robot.pop))

    def say_hi(self):
        print("Greetings, my master's call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots".format(cls.pop))

rob1 = robot("D2-R2")
rob2 = robot("AGNI")
rob3 = robot("INSAAS")

rob1.say_hi()
rob1.die()

robot.how_many()