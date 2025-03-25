#Заполнение матрицы по спирали
# n,m = list(map(int, input().split()))

#ввод параметров марицы
n = 4
m = 5
#заполнене матрицы нулями
matrix = [[0]*m for i in range(n)]
#обозначения граничных условий. максимальные значения сразу идут с минус 1
#i_min сразу задается с 1. считаем что прошли первую строку сразу
i_max = n-1
i_min = 1
j_max =m-1
j_min = 0

#начадоте направление движения
current_direction = 'right'
#координаты начальной точки. -1 потому что сразу проверяем словие и плюсуем
i, j = 0, -1
#цикл длинною с количество элементов. повороты по условию
for t in range(1, n*m+1):
    if current_direction == 'right':
        j = j +1
        if j == j_max:
            current_direction = 'down'
            j_max -= 1

    elif current_direction == 'left':
        j = j -1
        if j == j_min:
            current_direction = 'up'
            j_min += 1

    elif current_direction == 'up':
        i = i -1
        if i == i_min:
            current_direction = 'right'
            i_min += 1
    elif current_direction == 'down':
        i = i +1
        if i == i_max:
            current_direction = 'left'
            i_max -= 1

    #изменения значения марицы
    matrix[i][j] = t
#печать построчно
for i in matrix:
    print(*i)