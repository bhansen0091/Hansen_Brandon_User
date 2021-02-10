

class User:
    def __init__(self, name, email, initial_balance):
        self.name = name
        self.email = email
        self.account_balance = initial_balance

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        if amount > self.account_balance:
            print(f"{amount} cannot be withdrawn.  Current balance is ${self.account_balance}")
        else:
            self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def teansfer_money(self, amount, receiver_acct):
        self.account_balance -= amount
        receiver_acct.account_balance += amount
        return self


new_user_1 = User("newUser1", "newUser1@newUser.com", 10)
new_user_2 = User("newUser2", "newUser2@newUser.com", 10)
new_user_3 = User("newUser3", "newUser3@newUser.com", 10)

new_user_1.make_deposit(10).make_deposit(10).make_deposit(50).make_withdrawl(15).display_user_balance()

new_user_2.make_deposit(20).make_deposit(20).make_withdrawl(10).make_withdrawl(10).display_user_balance()

new_user_3.make_deposit(30).make_withdrawl(15).make_withdrawl(15).make_withdrawl(15).display_user_balance()

new_user_1.teansfer_money(15, new_user_3).display_user_balance()
new_user_3.display_user_balance()