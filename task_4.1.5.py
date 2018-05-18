"""
Напишите программу, которая реализует In-mapper combining v.2 для задачи WordCount в Hadoop Streaming.

Sample Input:

aut Caesar aut nihil
aut aut
de mortuis aut bene aut nihil

Sample Output:

aut	6
mortuis	1
bene	1
Caesar	1
de	1
nihil	2

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys
import collections

words = collections.Counter()
for line in sys.stdin:
    for word in line.strip().split(" "):
            words[word] += 1

for key, value in words.items():
    print(key + '\t' + str(value))
