def search_1(x, y, chislo):
    """Алгоритм бинарного поиска"""
    if chislo> y or chislo < x:
        return f"Число {chislo} не найдено в диапазоне от {x} до {y}"
    count = 0
    start = x
    finish = y
    #Закладываем медиану и проверяем начальные условия

    if chislo == start or chislo == finish:
        return f"Число соответсвует граничным условиям"
    # Если нет гоняем цикл до упаду
    while start <= finish:
        median = ((finish + start) // 2)
        if median == chislo:
            return f"Количество попыток = {count}, для поиска числа {chislo}"

        elif median > chislo:
            finish = median - 1

        else:
            start = median + 1

        count += 1






print(search_1(0,100,98))

