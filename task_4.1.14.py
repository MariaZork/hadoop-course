"""
Реализуйте mapper для задачи Cross-Correlation, который для каждого кортежа создает все пары элементов, входящих в него.
Mapper принимает на вход кортежи - строки, состоящие из объектов, разделенных пробелом.
Mapper пишет данные в виде key / value, где key - пара объектов, разделенных запятой, value - единица.

Sample Input:

a b
a b a c

Sample Output:

a,b	1
b,a	1
a,b	1
a,c	1
b,a	1
b,a	1
b,c	1
a,b	1
a,c	1
c,a	1
c,b	1
c,a	1

Программирование — Напишите программу. Тестируется через stdin → stdout
"""

import sys

for line in sys.stdin:
    letters = line.strip().split(" ")
    for x in letters:
        for y in letters:
            if x != y:
                print(x + ',' + y + '\t' + '1')

