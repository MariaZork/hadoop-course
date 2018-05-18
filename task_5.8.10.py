"""
Модифицируйте reducer из предыдущего задания так, чтобы он расcчитывал PageRank с учетом случайного перехода,
т.е. первого члена в формуле:
                            PR(x) = α * (1/N) + (1- α)*sum(PR(ti)/C(ti))
Для всех тестов считайте, что N = 5,  α = 0,1.

Входные и выходные данные: В качестве ключа идет номер вершины. Значение составное: через табуляцию записано
значение PageRank (округленное до 3-го знака после запятой) и список смежных вершин (через "," в фигурных скобках).

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

1	0.080	{2,4}
2	0.170	{3,5}
3	0.170	{4}
4	0.290	{5}
5	0.290	{1,2,3}

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys
import re

last_key = ''
summa, N, alpha = 0, 5, 0.1
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
        print('%s\t%.3f\t' % (last_key, alpha*(1/N) + (1 - alpha)*summa), end='')
        print('{' + ','.join(tmp_adjacency_list) + '}')
        summa = 0
        tmp_adjacency_list = re.findall(r'[\d]{1,3}', verticies)
        if verticies == '{}':
            summa = float(page_rank)

    last_key = num_vertice

if last_key:
    print('%s\t%.3f\t' % (last_key, alpha*(1/N) + (1 - alpha)*summa), end='')
    print('{' + ','.join(tmp_adjacency_list) + '}')
