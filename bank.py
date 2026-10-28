class BankAccount:
    MIN_BALANCE = 500

    def __init__(self, owner, balance=500):
        self.owner = owner
        if balance < BankAccount.MIN_BALANCE:
            print(f'Opening balance must be at least {BankAccount.MIN_BALANCE}. '
                  f'Set to {BankAccount.MIN_BALANCE}.')
            balance = BankAccount.MIN_BALANCE
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print('Enter a positive amount.')
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print('Enter a positive amount.')
            return False
        if self.__balance - amount < BankAccount.MIN_BALANCE:
            print(f'Cannot withdraw: balance must stay at least {BankAccount.MIN_BALANCE}.')
            return False
        self.__balance -= amount
        return True

    def get_balance(self):
        return self.__balance


def ask_amount(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print('Please enter a valid number.')
        return None

#Test 2: opening balance and privacy
acc2 = BankAccount('Test', 200)
print(acc2.get_balance())
print(acc2.owner)
try:
    print(acc2.__balance)
except AttributeError:
    print('AttributeError: the balance is private')

# Main program 
acc = BankAccount('Akshu', 1000)

while True:
    print('\n===== BANK =====')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Check balance')
    print('4. Exit')

    try:
        ch = int(input('Enter your choice: '))
    except ValueError:
        print('Invalid choice.')
        continue

    if ch == 1:
        amount = ask_amount('Amount to deposit: ')
        if amount is not None and acc.deposit(amount):
            print('Balance:', acc.get_balance())

    elif ch == 2:
        amount = ask_amount('Amount to withdraw: ')
        if amount is not None and acc.withdraw(amount):
            print('Balance:', acc.get_balance())

    elif ch == 3:
        print('Balance:', acc.get_balance())

    elif ch == 4:
        print('Goodbye!')
        break

    else:
        print('Invalid choice.')