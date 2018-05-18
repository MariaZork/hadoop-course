"""
Реализуйте reducer в задаче поиска кратчайшего пути с помощью Hadoop Streaming.

Входные и выходные данные: в качестве ключа идет номер вершины, значение состоит из двух полей, разделенных табуляцией:

Минимальное расстояние до данной вершины (если его еще нет, то пишется INF)
Список исходящих вершин (через "," в фигурных скобках).

Sample Input:

1	0	{2,3,4}
10	INF	{}
10	INF	{}
2	1	{}
2	1	{5,6}
3	1	{}
3	1	{}
4	1	{}
4	1	{7,8}
5	2	{}
5	INF	{9,10}
6	2	{}
6	INF	{}
7	2	{}
7	INF	{}
8	2	{}
8	INF	{}
9	INF	{}
9	INF	{}

Sample Output:

1	0	{2,3,4}
10	INF	{}
2	1	{5,6}
3	1	{}
4	1	{7,8}
5	2	{9,10}
6	2	{}
7	2	{}
8	2	{}
9	INF	{}

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys
import collections
import re

graph = collections.defaultdict()
last_vertice = ''
max_int = 10 ** 6
distances = list()

for line in sys.stdin:
    num_vertice, distance, adjacency_list = line.strip().split("\t")
    adjacency_list = re.findall(r'[\d]{1,3}', adjacency_list)

    if distance == 'INF':
        distance = max_int

    if not graph:
        graph[num_vertice] = [adjacency_list, int(distance)]
    elif last_vertice == num_vertice:
        distances.append(int(distance))
        adjacency_list += previous_adjacency_list
        graph[num_vertice] = [adjacency_list, min(distances)]
    else:
        distances = []
        graph[num_vertice] = [adjacency_list, int(distance)]

    last_vertice = num_vertice
    previous_adjacency_list = adjacency_list

for key, value in graph.items():
    if value[1] == max_int:
        print(key + '\t' + 'INF' + '\t' + '{' + ','.join(value[0]) + '}')
    else:
        print(key + '\t' + str(value[1]) + '\t' + '{' + ','.join(value[0]) + '}')
