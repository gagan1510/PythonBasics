class Account(object):
    "This is a simple class"
    num_accounts = 0
    def __init__(self, name, balance):
        "A new account is being created"
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts = -1

    def deposit(self, amt):
        "Add to the balance"
        self.balance += amt

    def withdraw(self,amt):
        "Subtract from balance"
        self.balance -= amt

    def inquire(self):
        print("\nThese are the details of the account holder:")
        print("Name:\t" + self.name)
        print("Balance:\t", self.balance)

class lowbal(Account):
    def islow(self):
        if self.balance < 500:
            return 'low bal'
        return 'appropriate bal'

    def tax(self):
        topay = (self.balance * 14.0/100)
        return topay

one = lowbal("Gagan", 1000)
one.deposit(500)
one.inquire()
one.withdraw(750)
one.inquire()
print("\nThe tax to be paid is: " + str(one.tax()))