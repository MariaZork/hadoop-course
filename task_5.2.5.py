"""
Реализуйте mapper в задаче поиска кратчайшего пути с помощью Hadoop Streaming.

Входные и выходные данные: в качестве ключа идет номер вершины, значение состоит из двух полей, разделенных табуляцией:

1. Минимальное расстояние до данной вершины (если его еще нет, то пишется INF)
2. Список исходящих вершин (через "," в фигурных скобках)

Sample Input:

1	0	{2,3,4}
2	1	{5,6}
3	1	{}
4	1	{7,8}
5	INF	{9,10}
6	INF	{}
7	INF	{}
8	INF	{}
9	INF	{}
10	INF	{}

Sample Output:

1	0	{2,3,4}
2	1	{}
3	1	{}
4	1	{}
2	1	{5,6}
5	2	{}
6	2	{}
3	1	{}
4	1	{7,8}
7	2	{}
8	2	{}
5	INF	{9,10}
9	INF	{}
10	INF	{}
6	INF	{}
7	INF	{}
8	INF	{}
9	INF	{}
10	INF	{}

Программирование — Напишите программу. Тестируется через stdin → stdout
"""

import sys
import collections
import re

graph = collections.defaultdict()

for line in sys.stdin:
    num_vertice, min_distance, adjacency_list = line.strip().split("\t")
    graph[num_vertice] = [min_distance, adjacency_list]

for key, value in graph.items():
    adjacency_vertices = re.findall(r'[\d]{1,3}', value[1])
    print(key + '\t' + value[0] + '\t' + value[1])

    if adjacency_vertices:
        for v in adjacency_vertices:
            if value[0] != 'INF':
                print(v + '\t' + str(int(value[0]) + 1) + '\t' + '{}')
            else:
                print(v + '\t' + value[0] + '\t' + '{}')
