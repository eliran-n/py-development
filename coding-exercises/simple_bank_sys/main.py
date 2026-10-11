
# 2043. Simple Bank System

class Bank(object):

    def __init__(self, balance):
        self.balance = balance
        self.balance_len = len(self.balance)

    def transfer(self, account1, account2, money):
        if account1 < 1 or account1 > self.balance_len:
            return False
        if account2 < 1 or account2 > self.balance_len:
            return False
        account1_index = account1 - 1
        account2_index = account2 - 1
        account1_balance = self.balance[account1_index]
        if account1_balance < money:
            return False
        self.balance[account1_index] = account1_balance - money
        self.balance[account2_index] = self.balance[account2_index] + money
        return True

    def deposit(self, account, money):
        if 1 > account or account > self.balance_len:
            return False
        account_balance = self.balance[account - 1]
        self.balance[account - 1] = account_balance + money
        return True

    def withdraw(self, account, money):
        if 1 > account or account > self.balance_len:
            return False
        account_index = account - 1
        account_balance = self.balance[account_index]
        if account_balance < money:
            return False
        else:
            self.balance[account_index] = self.balance[account_index] - money
            return True
