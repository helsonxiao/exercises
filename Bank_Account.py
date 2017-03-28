class BankAccount(object):
    def __init__(self, account_name, account_number, balance):
        if isinstance(account_name, str) and isinstance(account_number, (str, int)) and isinstance(balance, float):
            self.account_name = account_name
            self.account_number = account_number
            self.balance = balance

    def show_balance(self):
        print("You have " + str(self.balance) + " in your bank account.")

    def deposit(self):
        money = input("How much money do you want to deposit? ")
        if money:
            print("Done! Have a nice day, " + self.account_name + ".")

    def withdraw(self):
        money = input("How much money do you want to withdraw? ")
        if money:
            print("Done! Have a nice day, " + self.account_name + ".")


class InterestAccount(BankAccount):
    def __init__(self, account_name, account_number, balance, interest_rate):
        BankAccount.__init__(self, account_name, account_number, balance)
        self.interest_rate = interest_rate
        self.balance = balance
    def add_interest(self):
        self.balance = self.balance + self.balance * self.interest_rate
        print("A year passed. We added interest to your account.")


# my_account = BankAccount("Helson", 123, 10.5)
# my_account.show_balance()
# my_account.deposit()
# my_account.withdraw()

new_account = InterestAccount("Helson", 123, 100, 0.035)
time = 0
while time != 11111111:
    time += 1
new_account.add_interest()
new_account.show_balance()
