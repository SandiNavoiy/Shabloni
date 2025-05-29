


def sort_sliyanie(arr):
    """функция вызова рекурсии"""
    #базовый вариант. длина массива 0 или 1. 0 может быть , если до этого массив был не четной длинны
    if len(arr)<= 1:
        return arr
    #делим массив по условной середине
    middl = len(arr)//2
    #левая часть
    left= arr[:middl]
    #правая часть
    right=arr[middl:]

    #рекурсивный вывод. програма по рекурсии начинает дробить исходный массив дл базового случая
    # и потом склеивает результаты при помощи функции сорт
    return sort(sort_sliyanie(left), sort_sliyanie(right))


def sort(lst1, lst2):
    """функция склеивает массив"""
    #массив вывода
    rez = []
    #начальные индексы
    i = 0
    j = 0
    #перебор значений, меньшие вперед
    while i<len(lst1) and j < len(lst2):
        if lst1[i]< lst2[j]:
            rez.append(lst1[i])
            i = i+1
        else:
            rez.append(lst2[j])
            j = j + 1
    #добиваем остатки, хвосты массива
    while i<len(lst1):
        rez.append(lst1[i])
        i = i + 1
    #добиваем остатки, хвосты массива
    while j<len(lst2):
        rez.append(lst2[j])
        j = j + 1
    #вывод
    return rez



#начальные данные
lst = [8,11, -6, 3, 0, 1, 1]


#
print(sort_sliyanie(lst))
assert sort_sliyanie(lst) == [-6, 0, 1, 1, 3, 8, 11]

