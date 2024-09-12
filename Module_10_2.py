from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        for i in range(1, 101):
            if i * self.power <= 100:
                print(f'{self.name} сражается {i} день(дня)..., осталось {100 - i * self.power} воинов.')
                time.sleep(1)
            else:
                break
        print(f'{self.name} одержал победу спустя {i-1} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')