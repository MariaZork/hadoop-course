"""
Реализуйте reducer для алгоритма расчета PageRank с помощью Hadoop Streaming. Используйте упрощенный
алгоритм (без случайных переходов).

Входные и выходные данные: В качестве ключа идет номер вершины. Значение составное: через табуляцию записано значение
PageRank (округленное до 3-го знака после запятой) и список смежных вершин (через "," в фигурных скобках).

Sample Input:

1	0.067	{}
1	0.200	{2,4}
2	0.067	{}
2	0.100	{}
2	0.200	{3,5}
3	0.067	{}
3	0.100	{}
3	0.200	{4}
4	0.100	{}
4	0.200	{}
4	0.200	{5}
5	0.100	{}
5	0.200	{}
5	0.200	{1,2,3}

Sample Output:

1	0.067	{2,4}
2	0.167	{3,5}
3	0.167	{4}
4	0.300	{5}
5	0.300	{1,2,3}

Тесты:

Sample Input:

3	0.200	{}
3	0.400	{4,5}
3	0.500	{}
4	0.100	{2,5}
4	0.200	{}
4	0.200	{}

Sample Output:

3	0.700	{4,5}
4	0.400	{2,5}

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys
import re

last_key = ''
summa = 0
tmp_adjacency_list = ''

for line in sys.stdin:
    num_vertice, page_rank, verticies = line.strip().split("\t")
    if not last_key:
        last_key = num_vertice
        if verticies == '{}':
            summa = float(page_rank)
        tmp_adjacency_list = re.findall(r'[\d]{1,3}', verticies)
    elif last_key == num_vertice:
        tmp_adjacency_list = re.findall(r'[\d]{1,3}', verticies + str(tmp_adjacency_list))
        if verticies == '{}':
            summa += float(page_rank)
    else:
        adjacency_list = tmp_adjacency_list
        print('%s\t%.3f\t' % (last_key, summa), end='')
        print('{' + ','.join(tmp_adjacency_list) + '}')
        summa = 0
        tmp_adjacency_list = re.findall(r'[\d]{1,3}', verticies)
        if verticies == '{}':
            summa = float(page_rank)

    last_key = num_vertice

if last_key:
    print('%s\t%.3f\t' % (last_key, summa), end='')
    print('{' + ','.join(tmp_adjacency_list) + '}')
