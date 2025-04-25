import threading
import time

balance = 1000
lock = threading.Lock()

def withdraw_locked(name, amount):
    global balance
    print(f"{name} is trying to withdraw ₹{amount}")
    
    with lock:
        if balance >= amount:
            print(f"{name} - Approved")
            time.sleep(1)
            balance -= amount
            print(f"{name} - Withdrawn ₹{amount}, Remaining: ₹{balance}")
        else:
            print(f"{name} - Denied Insufficient balance")

# Threads
t1 = threading.Thread(target=withdraw_locked, args=("Alice", 700))
t2 = threading.Thread(target=withdraw_locked, args=("Bob", 500))

# Start threads
t1.start()
t2.start()

# Wait
t1.join()
t2.join()

print(f"\n🏦 Final Account Balance (with lock): ₹{balance}")
