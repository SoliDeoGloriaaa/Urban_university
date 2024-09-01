import random
import threading
import time


class Bank:

    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            random_dep = random.randint(50, 500)
            self.balance += random_dep
            print(f'Пополнение на {random_dep} | Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            random_take = random.randint(50, 500)
            print(f'Запрос на {random_take}')
            if random_take <= self.balance:
                self.balance -= random_take
                print(f'Снятие {random_take} | Баланс: {self.balance}')
            else:
                print('Запрос откланен, недостаточно средств.')
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')