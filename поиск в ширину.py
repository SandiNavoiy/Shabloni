from collections import deque
# водим количество вершин и ребер
versina, rebra = map(int, input().split())
# создаем скеелт для графа
graf = [[] for _ in range(versina)]
# забиваем таблицу смежности(вводим ребра)
for _ in range(rebra):
    a,b= map(int, input().split())
    graf[a].append(b)
    graf[b].append(a)
def bfs(graf, start, V):
    """функция поиска в ширину"""
    # Создаем список для хранения расстояний от начальной вершины
    spisok = [-1] * V
    # задаем начальную точку
    spisok[start] = 0
    # Создаём очередь и добавляем начальную вершину
    queue = deque()
    queue.append(start)
    # пока в очереди что то есть
    while queue:
        # вынимаем из очеерди первую вершину
        current = queue.popleft()
        # проходим по всем смежным вершинам
        for j in graf[current]:
            # песли вершига еше не посещена
            if spisok[j] == -1:
                # забивает расстояние от начальной вершины. ССУМИРУЕМ ВЕРШИНУ РОДИТЕЛЯ!!!!
                spisok[j] = spisok[current] + 1
                # Добавляем соседа в очередь
                queue.append(j)

    return  spisok


# Выводим результат
result = bfs(graf, 0, versina)
print(" ".join(map(str, result)))
