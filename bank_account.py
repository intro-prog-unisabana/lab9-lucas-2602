# bank_account.py
def __init__(self, account_number, balance=0.0):
    self.account_number = account_number
    self.balance = balance
def deposit(self, amount):
    self.balance = self.balance + amount
def withdraw(self, amount):
    if amount > self.balance:
        return -1
    else:
        self.balance = self.balance - amount
        return 0
def __str__(self):
    return f'Account Number: **{self.account_number[-2:]}\nCurrent Balance: {self.balance}'