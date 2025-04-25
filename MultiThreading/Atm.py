import threading
import time

account_balance = 1000
lock = threading.Lock()

def withdraw_money(name, amount):
    global account_balance
    print(f'{name} is trying to withdraw {amount}Rs...')

    with lock:
        if account_balance >= amount:
            print(f'{name} - Withdrawal Approved!')
            time.sleep(1)
            account_balance -= amount
            print(f'{name} - {amount}Rs withdrwan. Remaining balance: {account_balance}Rs')
        else:
            print(f'{name} - Withdrawal denied Insufficient balance')

user1 = threading.Thread(target=withdraw_money, args=("sahil", 200))
user2 = threading.Thread(target=withdraw_money, args=("Aditya", 700))
user3 = threading.Thread(target=withdraw_money, args=("Max", 2000))

user1.start()
user2.start()
user3.start()

user1.join()
user2.join()
user3.join()

print("\n All ATM transactions completed.")