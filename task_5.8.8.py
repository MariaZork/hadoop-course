"""
Реализуйте mapper для алгоритма расчета PageRank с помощью Hadoop Streaming.

Входные и выходные данные: В качестве ключа идет номер вершины. Значение составное: через табуляцию записано значение
PageRank (округленное до 3-го знака после запятой) и список смежных вершин (через "," в фигурных скобках).

Sample Input:

1	0.200	{2,4}
2	0.200	{3,5}
3	0.200	{4}
4	0.200	{5}
5	0.200	{1,2,3}

Sample Output:

1	0.200	{2,4}
2	0.100	{}
4	0.100	{}
2	0.200	{3,5}
3	0.100	{}
5	0.100	{}
3	0.200	{4}
4	0.200	{}
4	0.200	{5}
5	0.200	{}
5	0.200	{1,2,3}
1	0.067	{}
2	0.067	{}
3	0.067	{}

Программирование — Напишите программу. Тестируется через stdin → stdout
"""

import sys
import re

for line in sys.stdin:
    num_vertice, page_rank, verticies = line.strip().split("\t")
    adjacency_list = re.findall(r'[\d]{1,3}', verticies)
    print('%s\t%s\t%s' % (num_vertice, page_rank, verticies))
    if adjacency_list:
        page_rank = float(page_rank) / len(adjacency_list)
        for item in adjacency_list:
            print('%s\t%.3f\t%s' % (item, page_rank, '{}'))


