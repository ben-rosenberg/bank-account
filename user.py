class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def print_account_balance(self):
        print(f'User: {self.name}, Balance: ${self.account_balance}')
        return self
    def transfer(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

ben = User('Ben Rosenberg', 'ben@email.com')
daniel = User('Daniel Rosenberg', 'daniel@email.com')
emily = User('Emily Keene', 'emily@email.com')
ben.make_deposit(100).make_deposit(100).make_withdrawal(50).print_account_balance()
daniel.make_deposit(1200).make_deposit(800).make_withdrawal(300).make_withdrawal(200).print_account_balance()
emily.make_deposit(200).make_withdrawal(100).make_withdrawal(75).make_withdrawal(50).print_account_balance()

ben.transfer(emily, 100).print_account_balance()
emily.print_account_balance()