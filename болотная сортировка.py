import random
import time

#
colichestvo = 10


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

t1 = time.time()
print(boloto(colichestvo))
t2 = time.time()

print(f'{t2 - t1} секунд')