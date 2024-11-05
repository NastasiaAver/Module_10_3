import threading
import random
import time
from threading import Thread


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            add = random.randint(50, 500)
            self.balance += add
            print(f'Пополнение: {add}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            red = random.randint(50, 500)
            print(f'Запрос на {red}')
            if self.balance >= red:
                self.balance -= red
                print(f'Снятие: {red}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)




bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')