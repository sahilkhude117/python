import threading
import time

balance = 1000

def withdraw(name, amount):
    global balance
    print(f'{name} is trying to withdraw {amount}Rs')

    if balance >= amount:
        print(f'{name} - Approved!')
        time.sleep(2)
        balance -= amount
        print(f'{name} - withdrawn {amount}Rs, Remaining: {balance}Rs')
    else:
        print(f'{name} - Denied Insufficient Balance')


t1 = threading.Thread(target=withdraw, args=("sahil", 300))
t2 = threading.Thread(target=withdraw, args=("aditya", 800))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'\n Final Account Balance (without lock) {balance}Rs')