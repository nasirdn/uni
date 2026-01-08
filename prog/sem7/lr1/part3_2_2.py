import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount


account = BankAccount()

def worker():
    for _ in range(1000):
        account.deposit(15)
        account.withdraw(10)

threads = [threading.Thread(target=worker) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Баланс:", account.balance)