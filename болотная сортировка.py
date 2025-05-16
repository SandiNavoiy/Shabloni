import random
import time
from functools import wraps


def decor_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = time.time()
        f  = func(*args, **kwargs)
        time_end = time.time()
        print(f"Время выполнения функции составило {round(time_end -time_start, 10)} секунд")

        return f
    return wrapper
#
colichestvo = 5

@decor_time
def boloto(n):
    """Болотная сортировка, просто прикол"""
    lst = []
    # генерируем список из n случайных чисел от 1 до 100
    for i in range(n):
        lst.append(random.randint(1, 100))

    def prov(l):
        """функция проверки правильности сортировки"""
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                return False
        return True
    # перемешиваем список до тех пор, пока он не станет упорядоченным по возрастанию
    while True:
        if prov(lst):
            break
        else:
            random.shuffle(lst)

    return lst


print(boloto(colichestvo))


