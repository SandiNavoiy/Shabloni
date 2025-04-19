import time

a = 15
b = 121050



def get_nod(a,b):
    """Быстрый алгоритм Евклида нахождения НОД"""

    #надо чтобы а было всегода больше
    if b>a:
        a,b = b, a
#дальше большее заменяем меньшим а меньшее остатком от деления большего на меньшее
    while b !=0:
        a, b = b, a%b

#вывод НОД
    return a
start = time.time()
print(get_nod(a,b))
end = time.time()
print(end - start)
