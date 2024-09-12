import threading
import random
import time

lock = threading.Lock()
balance = random.randint(50, 500)

class Bank:

    def __init__(self):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        global balance
        for _ in range(100):
            d = random.randint(50, 500)
            balance += d
            if lock.locked() and balance >= 500:
                lock.release()
            print(f'Пополнение: {d}. Баланс: {balance}')
            time.sleep(0.001)

    def take(self):
        global balance
        for _ in range(100):
            t = random.randint(50, 500)
            print(f'Запрос на {t}')
            if t <= balance:
                balance -= t
                print(f'Снятие: {t}. Баланс: {balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                lock.acquire()

print(f'Начальный баланс: {balance}')

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk, ))
th2 = threading.Thread(target=Bank.take, args=(bk, ))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {balance}')