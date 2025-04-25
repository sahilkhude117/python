class BankAccount:
    def __init__(self, name, acc_number, balance=0):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount}Rs deposited successfully!')

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f'{amount}Rs withdrawn successfully!')

    def display_balance(self):
        print(f'Current balance; {self.balance}Rs')

    def display_info(self):
        print(f"Name: {self.name}, Account Number: {self.acc_number}, Balance: {self.balance}Rs")


bank_accounts = {}

def create_account():
    name = input("Enter name: ")
    acc_number = input("Enter account number: ")
    if acc_number in bank_accounts:
        print("Account already Exists! ")
    else:
        bank_accounts[acc_number] = BankAccount(name, acc_number)
        print("New account created successfully!")

def deposit_amount():
    acc_number = input("Enter account number: ")
    if acc_number in bank_accounts:
        amount = float(input("Enter amount to deposit: "))
        bank_accounts[acc_number].deposit(amount)
    else:
        print("Account not found!")

def withdraw_amount():
    acc_number = input("Enter account number: ")
    if acc_number in bank_accounts:
        amount = float(input("Enter amount to withdraw: "))
        bank_accounts[acc_number].withdraw(amount)
    else:
        print(" Account not found!")

def check_balance():
    acc_number = input("Enter account number: ")
    if acc_number in bank_accounts:
        bank_accounts[acc_number].display_balance()
    else:
        print("Account not found!")

def show_all_accounts():
    if bank_accounts:
        for account in bank_accounts.values():
            account.display_info()
    else:
        print("No accounts to display.")

while True:
    print("\n====== Bank Menu ======")
    print("1. New Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Show All Accounts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit_amount()
    elif choice == '3':
        withdraw_amount()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        show_all_accounts()
    elif choice == '6':
        print("👋 Exiting... Thank you for banking with us!")
        break
    else:
        print(" Invalid choice! Please try again.")