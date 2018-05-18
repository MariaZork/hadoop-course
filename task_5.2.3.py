"""
Реализуйте алгоритм Дейкстры поиска кратчайшего пути в графе.

Входные данные: В первой строке указаны два числа: число вершин и число ребер графа.
Далее идут строки с описанием ребер. Их количество равно числу ребер. В каждой строке указаны 3 числа:
исходящая вершина, входящая вершина, вес ребра. В последней строке указаны 2 номера вершины: начальная и
конечная вершина, кратчайший путь между которыми нужно найти.

Выходные данные: минимальное расстояние между заданными вершинами. Если пути нет, то нужно вернуть -1.

Sample Input:

4 8
1 2 6
1 3 2
1 4 10
2 4 4
3 1 5
3 2 3
3 4 8
4 2 1
1 4

Sample Output:

9

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys
import numpy as np

v1v2dist = []

for line in sys.stdin:
    v1v2dist.append((line.strip().split()))

num_vertices, num_ribs = v1v2dist[0][0], v1v2dist[0][1]
start_v, end_v = v1v2dist[len(v1v2dist) - 1][0], v1v2dist[len(v1v2dist) - 1][1]
v1v2dist.remove([num_vertices, num_ribs])
v1v2dist.remove([start_v, end_v])

dist = dict()
for v in range(1, int(num_vertices)+1):
    dist[str(v)] = np.inf
    dist[start_v] = 0

# ===работающий вариант====
Q = set(dist.keys())
answer = -1

while v1v2dist:
    nearest_vertice = min(Q, key=lambda x: dist[x])
    adjacent_vertices = [triplet for triplet in v1v2dist if nearest_vertice == triplet[0]]

    for item in adjacent_vertices:
        if dist[item[1]] > dist[nearest_vertice] + int(item[2]):
            dist[item[1]] = dist[nearest_vertice] + int(item[2])

    for item in adjacent_vertices:
        v1v2dist.remove(item)
    Q.remove(nearest_vertice)

answer = dist[end_v]
if answer != np.inf:
    print(int(answer))
else:
    print(-1)










