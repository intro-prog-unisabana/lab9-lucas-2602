# utils.py
from bank_account import BankAccount
from person import Person
def person_data():
    name = input("Enter the person's name:\n")
    person = Person(name)
    while continuar != "yes":
        account_number = input("Enter a 4-digit account number:\n")
        balance = ("Enter the initial balance:\n")
        bankAccount = BankAccount(account_number, balance)
        person.add_account(bankAccount)
        continuar = input("Are you done adding accounts? (yes/no):\n").lower()
    return person
def balance_summary(person_list):
    for person in person_list:
        total = 0
    for account in person.accounts:
        total = account.balance + total
    print(f"{person.name} : {total:.2f}")