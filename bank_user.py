

class User:
    def __init__(self, name, email, initial_balance):
        self.name = name
        self.email = email
        self.account = BankAccount(balance = initial_balance)

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def make_deposit(self, amount):
        self.account.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        if amount > self.account.account_balance:
            print(f"{amount} cannot be withdrawn.  Current balance is ${self.account.account_balance}")
        else:
            self.account.account_balance -= amount
        return self

    def teansfer_money(self, amount, receiver_acct):
        self.account.account_balance -= amount
        receiver_acct.account.account_balance += amount
        return self

class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.account_balance = balance
        self.interest_rate = int_rate

    def update_interest_rate(self, new_int_rate):
        self.interest_rate = new_int_rate
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = (self.account_balance + (self.account_balance * self.interest_rate))
        return self

    def display_account_info(self):
        print(f"Balance: {self.account_balance} | Interest Rate: {self.interest_rate}")
        return self

    # def deposit(self, amount):
    #     self.account_balance += amount
    #     return self

    # def withdraw(self, amount):
    #     if amount > self.account_balance:
    #         print("Insufficient funds")
    #     else:
    #         self.account_balance -= amount
    #     return self


new_user_1 = User("newUser1", "newUser1@newUser.com", 10)
new_user_2 = User("newUser2", "newUser2@newUser.com", 10)
new_user_3 = User("newUser3", "newUser3@newUser.com", 10)

new_user_1.display_user_balance()
new_user_1.make_deposit(100).make_withdrawl(10).account.display_account_info()
new_user_1.account.update_interest_rate(.05).display_account_info()

# new_user_1.make_deposit(10).make_deposit(10).make_deposit(50).make_withdrawl(15).display_user_balance()

# new_user_2.make_deposit(20).make_deposit(20).make_withdrawl(10).make_withdrawl(10).display_user_balance()

# new_user_3.make_deposit(30).make_withdrawl(15).make_withdrawl(15).make_withdrawl(15).display_user_balance()

# new_user_1.teansfer_money(15, new_user_3).display_user_balance()
# new_user_3.display_user_balance()